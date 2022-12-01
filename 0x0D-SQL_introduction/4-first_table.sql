-- creates a table called first_table in the current database in my mysql server
-- The database name will be passed as an argument of the mysql command
-- if first_table already exists, script should not fail
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
