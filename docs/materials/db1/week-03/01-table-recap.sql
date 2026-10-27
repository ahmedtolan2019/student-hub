-- Recap only. Skip this file if CampusLibrary and BookCopies already exist.
-- Select and execute one statement at a time, not the entire file.

CREATE DATABASE CampusLibrary;
GO
USE CampusLibrary;
GO
CREATE TABLE BookCopies (
    CopyId INT PRIMARY KEY,
    Title NVARCHAR(100) NOT NULL,
    Category NVARCHAR(40) NOT NULL,
    Shelf NVARCHAR(10) NOT NULL,
    IsAvailable BIT NOT NULL
);
