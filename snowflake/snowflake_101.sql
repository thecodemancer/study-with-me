#Data Warehouse
CREATE OR REPLACE WAREHOUSE DEMO WAREHOUSE_SIZE = "XSMALL",
MIN_CLUSTER_COUNT = 1,
MAX_CLUSTER_COUNT = 3,
AUTO_SUSPEND = 300,
AUTO_RESUME = TRUE;

#First Database
CREATE DATABASE our_first_database COMMENT = 'Our first database';

#Show Database
SHOW DATABASES LIKE 'our_first_database';

#Create database with retention time
CREATE DATABASE production_database DATA_RETENTION_TIME_IN_DAYS = 15 COMMENT = 'Critical production database';

SHOW DATABASES LIKE 'production_database';

#Database temporary
CREATE TRANSIENT DATABASE temporary_database DATA_RETENTION_TIME_IN_DAYS = 0 COMMENT = 'Temporary database for ETL processing';

SHOW DATABASES LIKE 'temporary_database';

#Alter database
ALTER DATABASE temporary_database
SET
    DATA_RETENTION_TIME_IN_DAYS = 1;

SHOW DATABASES LIKE 'temporary_database';

#Create table
CREATE TABLE customers (
        id INT NOT NULL,
        last_name VARCHAR(100),
        first_name VARCHAR(100),
        email VARCHAR(100),
        company VARCHAR(100),
        phone VARCHAR(100),
        address1 VARCHAR(150),
        address2 VARCHAR(150),
        city VARCHAR(100),
        state VARCHAR(100),
        postal_code VARCHAR(15),
        country VARCHAR(50)
    );
    
DESCRIBE TABLE customers;