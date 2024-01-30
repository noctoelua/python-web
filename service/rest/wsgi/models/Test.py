import sqlalchemy as sa
from config import config

from config import get_connection, Base


class TopAuthentication(Base):

    __tablename__ = "top_authentication"

    top_user = sa.Column("top_user", sa.VARCHAR(255), primary_key=True)
    top_user_name = sa.Column("top_user_name", sa.VARCHAR(255))
    top_password = sa.Column("top_password", sa.VARCHAR(255))
    lecturer_flg = sa.Column("lecturer_flg", sa.Boolean(255))
    inside_flg = sa.Column("inside_flg", sa.Boolean(255))


    @classmethod
    def get_top_user(cls, client_user, client_password):
        """index 画面のアクセス権限を確認
        """
        with get_connection() as session:
            top_list = list()
            for (
                top_user_name,
                lecturer_flg,
                inside_flg
            ) in session.query(
                cls.top_user_name,
                cls.lecturer_flg,
                cls.inside_flg
            ).filter(
                cls.top_user == client_user,
                cls.top_password == client_password
            ):
                top_list.append({
                    "top_user_name": top_user_name,
                    "lecturer_flg": lecturer_flg,
                    "inside_flg": inside_flg
                })

        return top_list
