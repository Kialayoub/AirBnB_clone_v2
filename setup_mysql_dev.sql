-- This script helps us prepare a MySQL server for the project

-- Creates a database named hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates a user hbnb_dev with the password hbnb_dev_pwd 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges on the hbnb_dev_db database to the user 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grants the SELECT privilege on the performance_schema table to the user 
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
