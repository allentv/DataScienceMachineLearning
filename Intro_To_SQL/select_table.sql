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


-- Simple join operation
-- Data from two tables are combined based on a lookup condition
-- Table aliases - t1, t2 are used to uniquely identify columns for each table
SELECT
    t1.First_Name, t1.Last_Name, t2.marks1, t2.marks2, t2.marks3
FROM
    student t1, marks t2
WHERE
    t1.ID = t2.Lookup_Key;


-- Sub-Query
-- The result of one select query is used to filter records of another query. 
-- The IN operator while check if the value of current record is present in
-- the list of values returned from the sub-query.
SELECT
    First_Name, Last_Name
FROM
    student
WHERE
    ID IN (
        SELECT Lookup_Key FROM marks WHERE marks1 IN (5, 10)
    );


-- Group By operation
-- The records are grouped based on the column 'Lookup_Key'
-- An aggregate operation SUM is applied to 3 columns - marks1, marks2, marks3
-- Display aliases are provided for the columns for better readability
SELECT
    Lookup_Key, SUM(marks1) 'Marks1 Total', SUM(marks2) 'Marks2 Total', SUM(marks3) 'Marks3 Total'
FROM
    marks
GROUP BY
    Lookup_Key;
