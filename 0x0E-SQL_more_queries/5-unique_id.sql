-- creates table unique_id with the description:
-- id INT with the default value 1 and unique, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
)
