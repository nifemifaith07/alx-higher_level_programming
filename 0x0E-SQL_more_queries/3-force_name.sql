-- creates table force_name with the following description
-- id INT, name VARCHAR(256) can’t be null
-- If force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
