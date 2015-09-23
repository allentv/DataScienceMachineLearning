-- Author : Allen Thomas Varghese
-- Date : 20-Sep-2015


-- Create a database first
CREATE DATABASE meetup;


-- Switch to the new database
USE meetup;


-- The below statement creates a table called 'table1' with 4 columns
CREATE TABLE student (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Age INT
);

CREATE TABLE marks (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Lookup_Key INT NOT NULL,
    marks1 INT,
    marks2 INT,
    marks3 INT,
    FOREIGN KEY marks(Lookup_Key) REFERENCES student(ID)
);

-- Add a new column 'comments'. The default value for this column would be NULL
ALTER TABLE marks ADD COLUMN comments VARCHAR(50);
ALTER TABLE marks DROP COLUMN comments;
