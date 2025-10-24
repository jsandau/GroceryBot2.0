/* 
Table creation.
*/

--DROP TABLE IF EXISTS grocery_requests; --

CREATE TABLE IF NOT EXISTS grocery_requests (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    name VARCHAR(50),
    item_name VARCHAR(100),
    quantity INT DEFAULT 1
);

SELECT * FROM grocery_requests;

--DROP TABLE IF EXISTS out_of_db; --

CREATE TABLE IF NOT EXISTS out_of_db (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    name VARCHAR(50),
    out_of VARCHAR(100)
);

SELECT * FROM out_of_db;
-- get all items that were out of that have also been requested-- 
SELECT item_name
FROM grocery_requests
WHERE item_name IN (
    SELECT out_of
    FROM out_of_db
);

CREATE TABLE IF NOT EXISTS weekly_grocery_summary (
    id SERIAL PRIMARY KEY,
    week DATE NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    quantity_ordered INT DEFAULT 0,
    request_count INT DEFAULT 0,
    is_staple BOOLEAN DEFAULT FALSE,
    was_out_of_stock BOOLEAN DEFAULT FALSE
);

SELECT * FROM weekly_grocery_summary;


