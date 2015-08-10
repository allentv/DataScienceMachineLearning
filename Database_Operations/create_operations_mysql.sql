-- Create database
CREATE DATABASE tutorial;

-- Make the new database active
USE tutorial;

-- Create a test table
CREATE TABLE `test_table` (
  `PK` int(11) NOT NULL AUTO_INCREMENT,
  `random_number` int(11) DEFAULT NULL,
  `comment` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PK`),
  UNIQUE KEY `PK_UNIQUE` (`PK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This is a test table';

-- Insert data into test_table
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (1,'c1');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (2,'c2');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (3,'c3');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (4,'c4');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (5,'c5');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (6,'c6');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (7,'c7');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (8,'c8');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (9,'c9');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (10,'c10');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (11,'c11');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (12,'c12');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (13,'c13');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (14,'c14');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (15,'c15');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (16,'c16');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (17,'c17');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (18,'c18');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (19,'c19');
INSERT INTO `test_table` (`random_number`, `comment`) VALUES (20,'c20');

-- Check if the number of records available are 20
SELECT 'Number of records available: ', COUNT(*) FROM `test_table`;
