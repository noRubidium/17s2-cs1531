CREATE TABLE Department (
  name varchar(50), -- text
  location varchar(50),
  MSSN int,
  Mdate time,
  PRIMARY KEY (name),
  FOREIGN KEY (MSSN) REFERENCES Employee(SSN)
);

CREATE TABLE Employee (
  SSN int,
  YEAR_OF_BIRTH time check (YEAR_OF_BIRTH < 2000 and YEAR_OF_BIRTH > 1900),
  Fname varchar(50),
  LName varchar(50),
  Dname varchar(50),
  PRIMARY KEY (SSN),
  FOREIGN KEY (Dname) REFERENCES Department(name),
);
