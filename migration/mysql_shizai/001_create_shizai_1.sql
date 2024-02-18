-- +migrate Up

CREATE TABLE shizai_1 (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `data1` varchar(255) DEFAULT NULL,
    `data2` varchar(255) DEFAULT NULL,
    `ins_datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `upt_datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- +migrate Down

DROP TABLE IF EXISTS shizai_1;
