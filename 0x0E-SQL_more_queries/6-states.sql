-- create the database hbtn_0d_usa
-- If the database hbtn_0d_usa already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create the table states (in the database hbtn_0d_usa) with description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- If the table states already exists, your script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
