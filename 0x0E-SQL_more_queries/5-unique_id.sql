-- A script that creates a table.
-- The query used create the table 'unique_id' in MySQL server.
-- If the table unique_id already exists, the script should not fail.

CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
