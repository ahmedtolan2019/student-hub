-- Optional practice extension. Requires the first six rows.
-- Run this INSERT once. The CSV contains all 36 rows, including the first six.
-- Viewing the CSV does not import it into SQL Server.
USE CampusLibrary;
GO

INSERT INTO BookCopies (CopyId, Title, Category, Shelf, IsAvailable)
VALUES (107, N'Data Structures', N'Computing', N'A3', 1),
       (108, N'Data Structures', N'Computing', N'A3', 0),
       (109, N'Computer Networks', N'Computing', N'A4', 1),
       (110, N'Computer Networks', N'Computing', N'A4', 1),
       (111, N'Operating Systems', N'Computing', N'A5', 0),
       (112, N'Operating Systems', N'Computing', N'A5', 1),
       (113, N'Intro to Circuits', N'Engineering', N'B1', 0),
       (114, N'Digital Logic', N'Engineering', N'B2', 1),
       (115, N'Digital Logic', N'Engineering', N'B2', 0),
       (116, N'Signals and Systems', N'Engineering', N'B3', 1),
       (117, N'Signals and Systems', N'Engineering', N'B3', 0),
       (118, N'Electronics Lab', N'Engineering', N'B4', 1),
       (119, N'Applied Mathematics', N'Mathematics', N'C1', 1),
       (120, N'Linear Algebra', N'Mathematics', N'C2', 1),
       (121, N'Linear Algebra', N'Mathematics', N'C2', 0),
       (122, N'Statistics Practice', N'Mathematics', N'C3', 1),
       (123, N'Statistics Practice', N'Mathematics', N'C3', 0),
       (124, N'Discrete Mathematics', N'Mathematics', N'C4', 1),
       (125, N'Physics Fundamentals', N'Science', N'D1', 1),
       (126, N'Physics Fundamentals', N'Science', N'D1', 0),
       (127, N'Chemistry in the Lab', N'Science', N'D2', 1),
       (128, N'Chemistry in the Lab', N'Science', N'D2', 0),
       (129, N'Scientific Writing', N'Science', N'D3', 1),
       (130, N'Scientific Writing', N'Science', N'D3', 0),
       (131, N'SQL Workbook', N'Computing', N'A2', 1),
       (132, N'SQL Workbook', N'Computing', N'A2', 0),
       (133, N'Algorithms in Practice', N'Computing', N'A3', 1),
       (134, N'Algorithms in Practice', N'Computing', N'A3', 0),
       (135, N'Engineering Mechanics', N'Engineering', N'B5', 1),
       (136, N'Engineering Mechanics', N'Engineering', N'B5', 0);
