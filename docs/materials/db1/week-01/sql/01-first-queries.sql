/*
  Database 1 - Week 1 / Lab 1
  01 - First queries (worked examples from the lab page, chapters 5 and 6)

  The question from the lending desk:
    "Is there a Computing book I can borrow right now? Which shelf is it on?"

  How to run ONE query in SSMS:
    1. Select the whole statement with the mouse (from SELECT to the semicolon).
    2. Press Execute on the toolbar, or F5.
    If nothing is selected, SSMS runs EVERYTHING in this editor, top to bottom.

  Before you start, the database dropdown on the SSMS toolbar should show
  Database1Lab01. If it shows master, choose Database1Lab01 there, or run the
  USE line below once.

  Every query in this file only READS. None of them changes the table.
  The data is fictional teaching data written for this lab.
*/

USE Database1Lab01;
GO
-- GO is not SQL. It is a line SSMS uses to split the file into batches; it is never sent to SQL Server.


/* ---------------------------------------------------------------------------
   Step 1 - Look at everything first
   * means "every column". ORDER BY CopyId makes the row order predictable;
   without ORDER BY, SQL Server does not promise any order.
   Expect 6 rows in Results, and "(6 rows affected)" in Messages.
--------------------------------------------------------------------------- */
SELECT *
FROM BookCopies
ORDER BY CopyId;


/* ---------------------------------------------------------------------------
   Step 2 - Only the columns the question needs
   "Which copy? Which shelf?"  ->  CopyId, Title, Shelf
   The table still has five columns. SELECT only chooses what to SHOW.
--------------------------------------------------------------------------- */
SELECT CopyId, Title, Shelf
FROM BookCopies
ORDER BY CopyId;


/* ---------------------------------------------------------------------------
   Step 3 - Keep only Computing copies
   N'Computing' is a Unicode string (NVARCHAR), the same kind of text as the
   Category column. The N matters for Arabic text; for plain English the query
   works without it too, but we write it to match the column.
   Predict first: which CopyIds survive?
--------------------------------------------------------------------------- */
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE Category = N'Computing'
ORDER BY CopyId;


/* ---------------------------------------------------------------------------
   Step 4 - Computing AND available right now
   AND keeps a row only when BOTH conditions are true.
   IsAvailable is a BIT: 1 = on the shelf now, 0 = lent out.
   This is the answer to the desk question.
--------------------------------------------------------------------------- */
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE Category = N'Computing'
  AND IsAvailable = 1
ORDER BY CopyId;


/* ===========================================================================
   Chapter 6 - Predict, then run
   Write your predicted CopyIds in the comment BEFORE you execute each query.
   =========================================================================== */

-- A. Every copy on the shelf right now.            My prediction: ____________
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE IsAvailable = 1
ORDER BY CopyId;

-- B. Computing copies on the shelf right now.     My prediction: ____________
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE Category = N'Computing'
  AND IsAvailable = 1
ORDER BY CopyId;

-- C. Copies that are lent out.                     My prediction: ____________
--    Look at the Shelf column: it is the copy's HOME shelf, even while it is out.
SELECT CopyId, Title, Shelf
FROM BookCopies
WHERE IsAvailable = 0
ORDER BY CopyId;

-- D. Every physical copy titled Database Design.  My prediction: ____________
--    Same title, different CopyIds: one row = one physical copy.
SELECT CopyId, Shelf, IsAvailable
FROM BookCopies
WHERE Title = N'Database Design'
ORDER BY CopyId;


/* ---------------------------------------------------------------------------
   Did the table change?
   Run step 1 again. Still 6 rows: SELECT reads, it never edits the table.
   The Results grid shows an answer; it is not a new table saved anywhere.
--------------------------------------------------------------------------- */
