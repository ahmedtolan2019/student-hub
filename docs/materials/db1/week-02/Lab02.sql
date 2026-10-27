-- Database 1 - Week 2 / Lab 2: build the library database yourself
-- Target script for the work-with-me lesson, with notes added.
-- Classroom checkpoint on 2026-10-27: table/types/constraints covered; INSERT starts this week.
--
-- Connect:  Server name .\SQLEXPRESS, Windows Authentication.
--           In SSMS 20 also tick "Trust server certificate".
--
-- The habit:  write a statement, SELECT it with the mouse, press F5.
--             If nothing is selected, F5 runs the WHOLE file again.
--
-- Do not run this file top to bottom on a PC where you already built
-- CampusLibrary: CREATE DATABASE, CREATE TABLE and INSERT will refuse to run
-- twice (Msg 1801, 2714, 2627). That refusal is SQL Server protecting your data.

-- 1. First lines. The answer comes back as a table in Results.
SELECT 2 + 3 AS Total;
SELECT 7 * 6 AS Answer;
-- Which database is this query tab using? A new tab starts in master.
SELECT DB_NAME() AS CurrentDatabase;

-- 2. Our own database. CREATE makes it; USE moves this tab into it.
--    Look at the database list on the toolbar after USE: CampusLibrary.
CREATE DATABASE CampusLibrary;
USE CampusLibrary;
SELECT DB_NAME() AS CurrentDatabase;

-- 3. The table: one row = one physical copy of a book.
--    INT whole number, NVARCHAR(n) Unicode text with a size limit, BIT for 0/1 here.
--    PRIMARY KEY: unique CopyId. NOT NULL rejects NULL, not an empty text string.
--    Commas go BETWEEN columns; the last column has none.
CREATE TABLE BookCopies (
    CopyId INT PRIMARY KEY,
    Title NVARCHAR(100) NOT NULL,
    Category NVARCHAR(40) NOT NULL,
    Shelf NVARCHAR(10) NOT NULL,
    IsAvailable BIT NOT NULL
);

-- An empty table: five column names, (0 rows affected).
SELECT * FROM BookCopies;

-- 4. The six copies. Text goes between single quotes with N in front: N'...'
--    "double quotes" mean a column name in SQL, not text (Msg 207).
--    Running the same INSERT twice gives Msg 2627: CopyId must be unique.
INSERT INTO BookCopies (CopyId, Title, Category, Shelf, IsAvailable)
VALUES (101, N'Python Basics', N'Computing', N'A1', 1);
INSERT INTO BookCopies (CopyId, Title, Category, Shelf, IsAvailable)
VALUES (102, N'Python Basics', N'Computing', N'A1', 0);
-- One INSERT, four rows, separated by commas: (4 rows affected).
INSERT INTO BookCopies (CopyId, Title, Category, Shelf, IsAvailable)
VALUES (103, N'Database Design', N'Computing', N'A2', 1),
       (104, N'Intro to Circuits', N'Engineering', N'B1', 1),
       (105, N'Applied Mathematics', N'Mathematics', N'C1', 0),
       (106, N'Database Design', N'Computing', N'A2', 0);

-- Why N? Without it, Arabic letters turn into ???? on the lab servers.
SELECT 'كتاب' AS WithoutN, N'كتاب' AS WithN;

-- 5. The desk question: "Is there a Computing book I can borrow now? Which shelf?"
--    AND keeps a row only when BOTH conditions are true. Answer: 101 (A1), 103 (A2).
--    With OR instead of AND you get 5 rows: no error, but the wrong answer.
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE Category = N'Computing'
  AND IsAvailable = 1;

-- Copies that are lent out, sorted by title: 105, 106, 102.
SELECT CopyId, Title
FROM BookCopies
WHERE IsAvailable = 0
ORDER BY Title;

-- On the lab servers, text comparison ignores upper/lower case: still 4 rows.
SELECT CopyId
FROM BookCopies
WHERE Category = N'computing';

-- 6. Save this file (Ctrl+S). Open New Query: the new tab starts in master,
--    so SELECT * FROM BookCopies; gives Msg 208 there.
--    Start that tab with USE CampusLibrary; and the six rows are still there:
--    the rows live in the database, not in this file.
