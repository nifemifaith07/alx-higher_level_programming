-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- You need to convert all of the following to UTF8:
-- convert database hbtn_0c_0
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert Table first_table
USE hbtn_0c_0;
ALTER TABLE first_table
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Field name in first_table
USE hbtn_0c_0;
ALTER TABLE first—tanle
CHANGE name name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci
