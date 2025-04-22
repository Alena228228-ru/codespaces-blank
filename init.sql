CREATE TABLE if not exists Orders (
    id INT primary key GENERATED ALWAYS AS IDENTITY,
    tg_id INT,
    name VARCHAR(20)
);
