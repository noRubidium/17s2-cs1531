-- Create table in sql
CREATE TABLE BOOK
    (ID INT PRIMARY KEY NOT NULL,
    TITLE TEXT NOT NULL,
    AUTHOR TEXT NOT NULL,
    YEAR TEXT,
    GENRE TEXT);

-- Insert records
INSERT INTO BOOK (ID,TITLE,AUTHOR,YEAR,GENRE) VALUES ('001', 'Agile Design Principles',
'Martin', '1996', 'Engineering Textbook');
INSERT INTO BOOK (ID,TITLE,AUTHOR,YEAR,GENRE) VALUES ('002', 'The Lord of the Rings',
'Tolkien', '1954', 'Fantasy');
INSERT INTO BOOK (ID,TITLE,AUTHOR,YEAR,GENRE) VALUES ('003', 'Pride and Prejudice', 'Jane',
'1813', 'Romance');
INSERT INTO BOOK (ID,TITLE,AUTHOR,YEAR,GENRE) VALUES ('004', 'The Great Gatsby', 'Scott',
'2004', 'Literary Fiction');
INSERT INTO BOOK (ID,TITLE,AUTHOR,YEAR,GENRE) VALUES ('005', 'Introduction to Cooking',
'Tom', '2016', 'Cook Book');
INSERT INTO BOOK (ID,TITLE,AUTHOR,YEAR,GENRE) VALUES ('006', 'SOLID in OO', 'Martin',
'2004', 'Design Guidebook');
