-- A script that creates the table force_name on the  MySQL server.
-- The DB name will be passed as an argument of the mysql command
-- If the table force_name already exists, the script should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT,
name VARCHAR(256) NOT NULL);
