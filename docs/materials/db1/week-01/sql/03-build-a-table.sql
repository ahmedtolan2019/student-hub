/*
  Database 1 - Week 1 / Lab 1
  03 - Build your own small table (guided, lab page chapter 8)

  You will make a reading wishlist: one row = one book title you want to read.
  It is a separate small table. BookCopies is not touched.

  Three different kinds of statement, three different habits:
    CREATE TABLE  makes the empty shape (the schema) ......... run it ONCE
    INSERT        adds new rows .............................. run each one ONCE
    SELECT        reads rows, changes nothing ................ run it as often as you like

  Run ONE statement at a time: select it with the mouse, then Execute (or F5).
  If nothing is selected, SSMS runs the whole file, including CREATE and INSERT again.

  This works on YOUR PC's own SQL Server (.\SQLEXPRESS), in Database1Lab01.
  If your class uses one shared server instead, use the database name your teacher
  gives you, so two students never create the same table in the same database.

  Saving this file (Ctrl+S) saves these instructions. It is NOT a backup of the
  table or its rows: those live in the database.
*/


/* ---------------------------------------------------------------------------
   Step 0 - Where am I?
   Run these two lines. The result must say Database1Lab01.
   If it says master, STOP: choose Database1Lab01 in the toolbar dropdown
   (or run the USE line again) before you create anything.
--------------------------------------------------------------------------- */
USE Database1Lab01;
SELECT DB_NAME() AS CurrentDatabase;


/* ---------------------------------------------------------------------------
   Step 1 - CREATE the table (run ONCE)
   Fill in the blanks, then run the whole CREATE TABLE statement.
     WishId : a whole number that identifies each wish, never repeated, never empty
     Title  : text, up to 100 characters, English or Arabic, must be present

   Hint: look at how CopyId and Title are declared in BookCopies
   (lab page, chapter 4).

   Expected in Messages: Commands completed successfully.
   Then in Object Explorer: right-click Database1Lab01 > Tables > Refresh,
   and look for ReadingWishlist.
--------------------------------------------------------------------------- */
CREATE TABLE ReadingWishlist (
    WishId  ________  ____________,
    Title   ________________  ________
);


/* ---------------------------------------------------------------------------
   Step 2 - INSERT two rows (run each statement ONCE)
   Replace the titles with books you actually want to read.
   The N before the quote makes the text Unicode, so Arabic titles work too.

   Expected in Messages after each one: (1 row affected)
--------------------------------------------------------------------------- */
INSERT INTO ReadingWishlist (WishId, Title)
VALUES (1, N'____________________');

INSERT INTO ReadingWishlist (WishId, Title)
VALUES (2, N'____________________');


/* ---------------------------------------------------------------------------
   Step 3 - SELECT them back (run as often as you like)
   Before you run it: how many rows do you expect? ____
--------------------------------------------------------------------------- */
SELECT WishId, Title
FROM ReadingWishlist
ORDER BY WishId;


/* ---------------------------------------------------------------------------
   Step 4 - Do the rows survive?
   1. Save this file (Ctrl+S), then close this query tab.
   2. Click New Query on the toolbar.
   3. Check the database dropdown says Database1Lab01.
   4. Type the SELECT from step 3 into the new tab and run it.

   Are the rows still there? ____  Where do they live? ______________________
--------------------------------------------------------------------------- */


/* ---------------------------------------------------------------------------
   Step 5 - Predict, then try: the same key twice
   Predict first: what will SQL Server do if you run the FIRST INSERT from
   step 2 again, unchanged (WishId 1 again)?

   My prediction: ______________________________________________

   Now select only that first INSERT in step 2 and run it again.
   Read the red message in Messages. Then run step 3 again: how many rows? ____

   Which rule from your CREATE TABLE caused this? ______________________
--------------------------------------------------------------------------- */


/* ---------------------------------------------------------------------------
   Step 6 - Your own row
   Write one more INSERT with a NEW WishId and a title of your choice.
   Run it once, then run step 3 again.
--------------------------------------------------------------------------- */



/*
  Something went wrong?
  - "There is already an object named 'ReadingWishlist' in the database."
      You ran CREATE TABLE a second time. The table is already there: go on to step 2.
      Do not delete the table to "start over"; ask your teacher if you are stuck.
  - "Invalid object name 'ReadingWishlist'."
      Wrong database selected (often master), or step 1 has not run successfully yet.
  - "Violation of PRIMARY KEY constraint ..."
      That WishId is already used. Choose a new number.
*/
