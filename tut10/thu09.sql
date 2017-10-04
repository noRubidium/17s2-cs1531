CREATE TABLE teacher (
  staff_no INT PRIMARY KEY
);

CREATE TABLE subject (
  subject_code INT PRIMARY KEY
);

CREATE TABLE teaching (
  subject_code INT NOT NULL,
  staff_no INT NOT NULL,
  semster INT NOT NULL,
  PRIMARY KEY (subject_code, staff_no),
  FOREIGN KEY (subject_code) REFERENCES subject(subject_code),
  FOREIGN KEY (staff_no) REFERENCES teach(staff_no)
);
