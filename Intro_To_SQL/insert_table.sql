-- Author : Allen Thomas Varghese
-- Date : 20-Sep-2015


-- Inserts 9 records into table 'student'
-- The values are inserted in the same order as the list of columns
-- The 'ID' column is an auto increment column & so a value cannot be assigned
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U1', 'U11', 11);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U2', 'U22', 22);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U3', 'U33', 33);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U4', 'U44', 44);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U5', 'U55', 55);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U6', 'U66', 66);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U7', 'U77', 77);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U8', 'U88', 88);
INSERT INTO student (First_Name, Last_Name, Age) VALUES ('U9', 'U99', 99);
INSERT INTO student (First_Name, Last_Name)      VALUES ('U10', 'U100');


-- Insert 7 records into table 'marks'
-- Records are inserted only for 3 users - U1, U2, U3
INSERT INTO marks (Lookup_Key, marks1, marks2, marks3) VALUES (1, 11, 22, 33);
INSERT INTO marks (Lookup_Key, marks1, marks2, marks3) VALUES (1, 11, 22, 33);
INSERT INTO marks (Lookup_Key, marks1, marks2, marks3) VALUES (1, 11, 22, 33);
INSERT INTO marks (Lookup_Key, marks1, marks2, marks3) VALUES (2, 5, 5, 5);
INSERT INTO marks (Lookup_Key, marks1, marks2, marks3) VALUES (2, 5, 5, 5);
INSERT INTO marks (Lookup_Key, marks1, marks2, marks3) VALUES (2, 5, 5, 5);
INSERT INTO marks (Lookup_Key, marks1, marks2, marks3) VALUES (3, 10, 20, 30);
