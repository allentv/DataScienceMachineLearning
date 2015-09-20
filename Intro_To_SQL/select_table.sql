-- Author : Allen Thomas Varghese
-- Date : 20-Sep-2015


-- The below statement selects all records with all columns from the table 'student'
SELECT * FROM student;


-- The below statement selects all records with data 
-- from only 2 columns - ID and Age, from the table 'student'
SELECT ID, Age FROM student;


-- The below statement selects 5 records from table 'student'
SELECT * FROM student LIMIT 5;


-- Fetch the records in descending order for 'Age' column
SELECT * FROM student ORDER BY Age DESC;


-- Apply a condition on the Age column
SELECT * FROM student WHERE Age > 50;


-- Apply multiple conditions with operators
SELECT * FROM student WHERE Age > 50 AND ID <= 90;


-- Apply functions

-- Get the number of records for the 'Age' column
SELECT COUNT(Age) FROM student;

-- Compute the sum of values in the 'Age' column
SELECT SUM(Age) FROM student;

-- Get the maximum value for the 'ID' column
SELECT MAX(ID) FROM student;

-- Get the minimum value for the 'ID' column
SELECT MIN(ID) FROM student;


-- The generic way to get the number of records of a table
-- Calling COUNT() on a column does not include NULL values
SELECT COUNT(*) FROM student;


-- Fetch the records with empty (NULL) values in the 'Age' column
SELECT * FROM student WHERE Age IS NULL;
