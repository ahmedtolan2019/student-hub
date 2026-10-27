/*
  Database 1 - Week 1 / Lab 1
  02 - Your turn (independent tasks)

  Same table as the lab: BookCopies in database Database1Lab01.

    CopyId | Title               | Category    | Shelf | IsAvailable
    -------+---------------------+-------------+-------+------------
       101 | Python Basics       | Computing   | A1    | 1
       102 | Python Basics       | Computing   | A1    | 0
       103 | Database Design     | Computing   | A2    | 1
       104 | Intro to Circuits   | Engineering | B1    | 1
       105 | Applied Mathematics | Mathematics | C1    | 0
       106 | Database Design     | Computing   | A2    | 0

    One row = one physical copy. IsAvailable: 1 = on the shelf now, 0 = lent out.
    Shelf = the copy's home shelf (it keeps it while the copy is lent out).

  For every task:
    1. Write your PREDICTION first (which CopyIds, in which order).
    2. Write the query under the task.
    3. Select only your query, press Execute (or F5), and compare with your prediction.
    4. If they differ, find out why before you change anything.

  Every task only needs SELECT. Do not change BookCopies.
  Save your work with File > Save (Ctrl+S). Saving keeps your queries, not the data.
*/

USE Database1Lab01;
GO


/* ---------------------------------------------------------------------------
   Task 1 - Only some columns
   Show the Title and Shelf of every copy, in CopyId order.

   My prediction (how many rows?): ____
--------------------------------------------------------------------------- */




/* ---------------------------------------------------------------------------
   Task 2 - Gaps on the shelves
   Which home shelves are missing a copy right now?
   Show Shelf and CopyId for every copy that is lent out, ordered by Shelf.

   My prediction (CopyIds in order): ______________________
--------------------------------------------------------------------------- */




/* ---------------------------------------------------------------------------
   Task 3 - Two conditions
   Show CopyId and Shelf of the Computing copies that are lent out,
   in CopyId order.

   My prediction: ______________________
--------------------------------------------------------------------------- */




/* ---------------------------------------------------------------------------
   Task 4 - One title, several copies
   Show CopyId and IsAvailable of every physical copy titled Python Basics,
   in CopyId order.

   My prediction: ______________________

   Then answer here:
     How many copies of this title does the desk own? ____
     Can a student borrow one right now? Which CopyId? ____
     Why does the table need CopyId when the title is already there?
     ______________________________________________________________
--------------------------------------------------------------------------- */




/* ---------------------------------------------------------------------------
   Task 5 - Alphabetical list
   Show Title and CopyId of all copies, ordered by Title (A to Z).
   Copies with the same title should appear in CopyId order.

   My prediction (CopyIds in order): ______________________
--------------------------------------------------------------------------- */




/* ---------------------------------------------------------------------------
   Task 6 - Explain a mistaken result
   A classmate wanted "Computing copies that are available" and wrote:

     SELECT CopyId, Title
     FROM BookCopies
     WHERE Category = N'Computing' OR IsAvailable = 1
     ORDER BY CopyId;

   They got 101, 102, 103, 104, 106.

   a) Why are 102 and 106 in the result?
      ______________________________________________________________
   b) Why is 104 in the result?
      ______________________________________________________________
   c) Write the corrected query below and check that it answers the question.
--------------------------------------------------------------------------- */




/* ---------------------------------------------------------------------------
   Task 7 - Empty, but no error
   This query runs, shows zero rows and no red error message:

     SELECT CopyId, Title
     FROM BookCopies
     WHERE Category = N'Maths';

   a) Why zero rows? (Look at the data, not the syntax.)
      ______________________________________________________________
   b) Is "zero rows" an error? ________
   c) Write a query that lists the mathematics copies.
--------------------------------------------------------------------------- */




/* ---------------------------------------------------------------------------
   Task 8 - Design thinking (no SQL to run)
   The campus equipment room keeps a list of laptops lent to labs:

     AssetTag | Model       | Room
     ---------+-------------+------
     L-07     | NoteBook 14 | Lab 2
     L-08     | NoteBook 14 | Lab 2
     L-12     | NoteBook 15 | Lab 5

   Laptop L-08 is moved to Lab 5.

   a) What does one row describe?
      ______________________________________________________________
   b) Someone suggests Model as the PRIMARY KEY. What goes wrong?
      ______________________________________________________________
   c) Which column should be the key? Which value(s) change when L-08 moves?
      ______________________________________________________________
--------------------------------------------------------------------------- */



/* ---------------------------------------------------------------------------
   Extra (if you finish early)
   Write one question a desk worker might ask that BookCopies CAN answer,
   with its query. Then write one question it CANNOT answer, and say what
   information is missing from the table.
--------------------------------------------------------------------------- */
