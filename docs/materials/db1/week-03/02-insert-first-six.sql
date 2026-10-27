-- Start here this week after the table exists. Run each INSERT once.
-- The column list matches the order of the values.
USE CampusLibrary;
GO

INSERT INTO BookCopies (CopyId, Title, Category, Shelf, IsAvailable)
VALUES (101, N'Python Basics', N'Computing', N'A1', 1);

INSERT INTO BookCopies (CopyId, Title, Category, Shelf, IsAvailable)
VALUES (102, N'Python Basics', N'Computing', N'A1', 0);

INSERT INTO BookCopies (CopyId, Title, Category, Shelf, IsAvailable)
VALUES (103, N'Database Design', N'Computing', N'A2', 1),
       (104, N'Intro to Circuits', N'Engineering', N'B1', 1),
       (105, N'Applied Mathematics', N'Mathematics', N'C1', 0),
       (106, N'Database Design', N'Computing', N'A2', 0);

SELECT * FROM BookCopies ORDER BY CopyId;
