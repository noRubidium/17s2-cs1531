CREATE TABLE Department (
  name varchar(50),
  location varchar(50),
  managerSSN int,
  mDate date,
  PRIMARY KEY (name),
  FOREIGN KEY (managerSSN) REFERENCES Employee(SSN)
);
CREATE TABLE Employee (
  SSN int,
  DOB date,
  FNAME varchar(50),
  LNAME varchar(50),
  departmentName varchar(50),
  PRIMARY KEY (SSN),
  FOREIGN KEY (departmentName) REFERENCES Department(name)
);

CREATE TABLE Project (
  ProjectNumber int,
  PRIMARY KEY(ProjectNumber)
);

CREATE TABLE Participation (
  ProjectNumber int,
  EmployeeSSN int,
  participationTime date,
  PRIMARY KEY (ProjectNumber, EmployeeSSN),
  FOREIGN KEY (ProjectNumber) REFERENCES Project(ProjectNumber),
  FOREIGN KEY (EmployeeSSN) REFERENCES Employee(SSN)
);
