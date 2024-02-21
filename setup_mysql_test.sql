

-- Creates a database named hbnb_test_db if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a database named performance_schema if it does not already exist
CREATE DATABASE IF NOT EXISTS performance_schema;

-- Creates a user hbnb_test with the password hbnb_test_pwd if it does not already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on the hbnb_test_db database to the user hbnb_test on localhost
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants the SELECT privilege on all tables in the performance_schema database to the user hbnb_test on localhost
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

