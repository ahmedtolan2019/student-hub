-- Run after the first six rows. The video later repeats the questions on all 36.
USE CampusLibrary;
GO

-- all_rows
SELECT * FROM BookCopies ORDER BY CopyId;

-- selected_columns
SELECT CopyId, Title, Shelf FROM BookCopies ORDER BY CopyId;

-- computing
SELECT CopyId, Title, Shelf, IsAvailable
FROM BookCopies
WHERE Category = N'Computing'
ORDER BY CopyId;

-- available_computing
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE Category = N'Computing'
  AND IsAvailable = 1
ORDER BY Title, CopyId;

-- or_trap
SELECT CopyId, Title, Category, IsAvailable
FROM BookCopies
WHERE Category = N'Computing'
   OR IsAvailable = 1
ORDER BY CopyId;

-- two_categories
SELECT CopyId, Title, Category
FROM BookCopies
WHERE Category = N'Computing'
   OR Category = N'Mathematics'
ORDER BY Category, Title, CopyId;

-- unavailable
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE IsAvailable = 0
ORDER BY Title, CopyId;

-- shelf_a2
SELECT CopyId, Title, IsAvailable
FROM BookCopies
WHERE Shelf = N'A2'
ORDER BY Title, CopyId;

-- title_copies
SELECT CopyId, Title, Shelf, IsAvailable
FROM BookCopies
WHERE Title = N'Database Design'
ORDER BY CopyId;

-- available_engineering
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE Category = N'Engineering'
  AND IsAvailable = 1
ORDER BY Title, CopyId;

-- descending_ids
SELECT CopyId, Title
FROM BookCopies
ORDER BY CopyId DESC;
