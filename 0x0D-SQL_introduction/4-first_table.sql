-- creates a table called first_table in the current database in my mysql server
-- The database name will be passed as an argument of the mysql command
-- script should not fail if first_table already exists
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
