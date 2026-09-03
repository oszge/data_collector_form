DROP TABLE IF EXISTS personal_details CASCADE;
DROP TABLE IF EXISTS address_information CASCADE;
DROP TABLE IF EXISTS education CASCADE;
DROP TABLE IF EXISTS employment CASCADE;



CREATE TABLE personal_details
(
person_id SERIAL PRIMARY KEY, 
first_name VARCHAR(100) NOT NULL, 
middle_name VARCHAR(100), 
last_name VARCHAR(100) NOT NULL, 
date_of_birth DATE NOT NULL, 
gender VARCHAR(100) NOT NULL, 
CONSTRAINT chk_gender 
    CHECK (gender IN ('Male', 'Female', 'Other')), 
phone_number VARCHAR(150) NOT NULL, 
email_address VARCHAR(150) NOT NULL
);

CREATE TABLE address_information
(
address_id SERIAL PRIMARY KEY, 
adrs_person_id INTEGER NOT NULL UNIQUE, 
CONSTRAINT fk_address_person_id 
    FOREIGN KEY(adrs_person_id) 
    REFERENCES personal_details(person_id)
    ON DELETE CASCADE,
address_line_1 VARCHAR(150) NOT NULL, 
address_line_2 VARCHAR(150),
city VARCHAR(50) NOT NULL, 
state_province VARCHAR(100), 
postal_code_zip_code VARCHAR(100) NOT NULL, 
country VARCHAR(100) NOT NULL
);

CREATE TABLE education
(
education_id SERIAL PRIMARY KEY, 
edu_person_id INTEGER NOT NULL UNIQUE,
CONSTRAINT fk_edu_person_id
    FOREIGN KEY(edu_person_id) 
    REFERENCES personal_details(person_id)
    ON DELETE CASCADE,
highest_level_of_education VARCHAR(150) NOT NULL, 
institution VARCHAR(150) NOT NULL, 
year_of_graduation INT NOT NULL,
CONSTRAINT chk_year_of_graduation
    CHECK (year_of_graduation BETWEEN 1900 AND 2100)
);

CREATE TABLE employment
(
employment_id SERIAL PRIMARY KEY, 
emp_person_id INTEGER NOT NULL UNIQUE,
CONSTRAINT fk_emp_person_id
    FOREIGN KEY(emp_person_id)
    REFERENCES personal_details(person_id)
    ON DELETE CASCADE,
current_employment_status VARCHAR(100) NOT NULL, 
job_position VARCHAR(100), 
company_org VARCHAR(100)
);

SELECT * FROM personal_details;
SELECT * FROM address_information;

TRUNCATE TABLE
    employment,
    education,
    address_information,
    personal_details
RESTART IDENTITY CASCADE;