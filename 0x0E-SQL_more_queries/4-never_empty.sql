-- A script that creates a table.
-- The query used to create the table 'id_not_null' in MySQL server.
--database name will be passed as an argument of the mysql command.

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
