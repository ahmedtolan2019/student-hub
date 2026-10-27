DB1: BookCopies practice data

This is a fictional college library dataset, not data from a real institution.
One row is one physical book copy. Repeated titles have different CopyId values.
IsAvailable: 1 = available, 0 = unavailable.

The class previously created CampusLibrary and BookCopies.
1. Skip 01-table-recap.sql if the database/table already exist.
2. Open 02-insert-first-six.sql and run one selected INSERT at a time, once.
3. Run SELECT to inspect the first six rows.
4. 03-expand-to-36.sql optionally adds 30 more copies once.
5. 04-questions.sql contains the reading/filtering/sorting examples.

BookCopies.csv has ALL 36 copies, including the first six. Opening it does not import it.
Do not import all 36 on top of the first six; their primary keys would duplicate.
The CSV is supplied to inspect and predict results. Use the provided INSERT scripts for this lesson.

These scripts never delete or overwrite your existing database. Repeating CREATE or INSERT can produce an error. Read it and inspect the current database before proceeding.
No UPDATE, DELETE or table relationships are part of this lesson.
