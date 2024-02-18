import sqlalchemy as sa
from config import config

from config import get_connection, Base
from libs.Decorators import db_log


class Shizai1(Base):
    __tablename__ = "shizai_1"

    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    data1 = sa.Column("data1", sa.VARCHAR(255))
    data2 = sa.Column("data2", sa.VARCHAR(255))
    ins_datetime = sa.Column("ins_datetime", sa.DateTime)
    upt_datetime = sa.Column("upt_datetime", sa.DateTime)


    @classmethod
    @db_log(alert_limit=0.01)
    def get_shizai1_all(cls):
        ret_dict = {}
        with get_connection() as session:
            for (
                id,
                data1,
                data2,
                ins_datatime,
                upt_datetime
            ) in session.query(
                cls.id,
                cls.data1,
                cls.data2,
                cls.ins_datetime,
                cls.upt_datetime
            ).all():
                ret_dict[id] = {
                    "data1": data1,
                    "data2": data2,
                    "ins_datetime": ins_datatime.strftime('%Y/%m/%d %H:%M:%S.%f'),
                    "upt_datetime": upt_datetime.strftime('%Y/%m/%d %H:%M:%S.%f')
                }
        return ret_dict
