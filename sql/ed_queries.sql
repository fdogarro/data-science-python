-- Drop databases if exist


DROP DATABASE IF EXISTS nj_state_teachers_salaries;
DROP DATABASE IF EXISTS teacher_sample;


-- Create the table if it doesn't exit
CREATE SCHEMA IF NOT EXISTS nj_state_teachers_salaries;


-- Create the table
CREATE TABLE IF NOT EXISTS nj_state_teachers_salaries.new_nj_state_teachers_salaries(
  last_name               VARCHAR(100),
  first_name              VARCHAR(100),
  county                  VARCHAR(100),
  district                VARCHAR(100),
  school                  VARCHAR(100),
  primary_job             VARCHAR(200),
  fte                     FLOAT,
  salary                  FLOAT,
  certificate             VARCHAR(100),
  subcategory             VARCHAR(100),
  teaching_route          VARCHAR(100),
  highly_qualified        VARCHAR(100),
  experience_district     INT,
  experience_nj           INT,
  experience_total        INT
);


-- Load CSV data into table
LOAD DATA LOCAL INFILE '/Users/feliciaogarro/Dumps/new_nj_state_teachers_salaries.csv'
INTO TABLE nj_state_teachers_salaries.new_nj_state_teachers_salaries
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- Create random sample and dump the results to a CSV file
SELECT "last_name", "first_name", "county", "district", "school", "primary_job",
"fte", "salary", "certificate", "subcategory", "teaching_route", "highly_qualified", "experience_district",
"experience_nj", "experience_total"
UNION
(SELECT DISTINCT last_name, first_name, county, district, school, primary_job,
fte, salary, certificate, subcategory, teaching_route, highly_qualified, experience_district, experience_nj, experience_total
FROM nj_state_teachers_salaries.new_nj_state_teachers_salaries
ORDER BY RAND(7)
LIMIT 777)
INTO OUTFILE '/Users/feliciaogarro/Dumps/teachersample.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';


-- Create the table if it doesn't exit
CREATE SCHEMA IF NOT EXISTS teacher_sample;


-- Create teacher_sample.teachers table
CREATE TABLE IF NOT EXISTS teacher_sample.teachers(
  last_name               VARCHAR(100),
  first_name              VARCHAR(100),
  county                  VARCHAR(100),
  district                VARCHAR(100),
  school                  VARCHAR(100),
  primary_job             VARCHAR(200),
  fte                     FLOAT,
  salary                  FLOAT,
  certificate             VARCHAR(100),
  subcategory             VARCHAR(100),
  teaching_route          VARCHAR(100),
  highly_qualified        VARCHAR(100),
  experience_district     INT,
  experience_nj           INT,
  experience_total        INT
);


-- Load the data into a SQL table
LOAD DATA INFILE '/Users/feliciaogarro/Dumps/teachersample.csv'
INTO TABLE teacher_sample.teachers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- Calculate average salary
SELECT AVG(salary) from teacher_sample.teachers;


-- Calculate the number of people whose salary is more than 150,000
SELECT COUNT(*) from teacher_sample.teachers WHERE salary > 150000;


-- Get the last name of the ones who make more than 150,000 but has less than 5 years of total experience
SELECT last_name, salary, experience_total from teacher_sample.teachers WHERE salary > 150000 AND experience_total < 5;


-- Get the highest salary for Preschool, School Counselor, Principal, School Psychologist, and Kindergarten.
SELECT primary_job, MAX(salary) as max_salary from teacher_sample.teachers
WHERE primary_job LIKE "Preschool"
OR primary_job LIKE "School Counselor"
OR primary_job LIKE "Principal"
OR primary_job LIKE "School Psychologist"
OR primary_job LIKE "Kindergarten"
GROUP BY primary_job;


-- Get the last name, first name, and salary of the lowest earner who works in Atlantic City
SELECT first_name, last_name, district, salary from teacher_sample.teachers
WHERE salary = (SELECT MIN(salary) FROM teacher_sample.teachers WHERE district = 'Atlantic City');


-- Get the total number of employees working in Passaic City with more than ten years of total experience.
SELECT COUNT(*) from teacher_sample.teachers WHERE district = 'Passaic City' AND experience_total > 10;
