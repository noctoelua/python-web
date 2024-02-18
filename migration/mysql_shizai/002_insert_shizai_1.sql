-- +migrate Up

INSERT INTO
    shizai_1 (`data1`, `data2`)
VALUES
    ('row 1', 'test1'),
    ('row 2', 'test2');

-- +migrate Down

DELETE FROM shizai_1;
