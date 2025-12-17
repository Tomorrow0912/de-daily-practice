05-12-2025 - SQL Practice

Purpose:
Learn SQL foundational operations using SQLite and perform Create Read Update and Delete functions.

Exercises completed
- created character table
- inserted multiple rows
- queried data using SELECT statement
- updated rows based on conditions 
- explored SQLite default case sensitivity
- verified database selected

Key Learnings:
- SQL string comparisons are case sensitive by default
- Sorting uses ASCII (uppercase before lowercase)
- missing semicolons cause multi-line issues
- Quoting must be correct for SQLite to interpret values as strings
- importance of using .databases to verify current database

Next Steps:
- Working with multi table functionality
- Modifying table schema
- deleting data efficiently and safely



08-12-2025 - python cleaning

Purpose:
Use the Pandas module to load structured data, apply simple transformations, and preview the results within Python.

Exercises completed:
- created a virtual environment for the session
- installed required modules and verified environment isolation
- loaded an existing CSV into a Panda DataFrame
- converted a selected column to lower case
- output a transformed subset column of data for validation

Lessons:
- how to create, activate and work within a virtual environment
- correct script structure using top to bottom workflow
- how pandas reads a CSV and returns data

Next steps:
- remove white spaces
- explore handling of missing or null values
- write data back into the CSV


09-12-2025 - python cleaning V2

Purpose:
Further transform and clean the data, perform fundamentals of ETL

Exercises completed:
- removed trailing spaces from data
- export cleaned data to a new csv
- print both raw and cleaned data for comparison
- added handling for null items

Lessons:
- importance of using quotation marks for text
- use of "index = false" in to.csv to prevent unamed columns

Next steps:
- validate data types for each column
- add a derived field, for example boolean
- introduce error handling around file loading and saving


10-12-2025 - SQL Joins

Purpose:
Create a secondary table within a singular SQLite datavase, and utilise SQL Inner-Joins to merge the data

Exercises completed:
- created a weapons table with its own primary key and a character_id field referencing characters.id
- inserted weapon rows linked to existing character IDs
- queried characters and weapons together using an INNER JOIN

Lessons:
- Importance of using a unique ID
- How to drop a table created in error
- JOIN returns a combined result set, it does not modify tables
- both tables must live in the same database file

Next Steps:
- LEFT and RIGHT join practices
- Filtering and conditions on JOINS
- Data Validation Queries


12-12-2025 Python Cleaning V3

Purpose: Add data validation, parsing, and a boolean flag

Exercises completed:
- Convert a column into an int data type and catching manually added errors
- create a boolean flag that reads a column and returns a true/false value

Lessons learned:
- In booleans '==' compares, '=' verifies
- Using try/except to handle parsing errors without crashing the script

Next steps:
- Add lightweight validation reporting (count invalid rows, print which rows failed)
- Decide a consistent strategy for invalid numeric values (drop vs fill with a default)

17-12-2025 Python Cleaning V4

Purpose: Add error catching and termination when required

Exercises completed:
- imported sys
- have the system exit if the read fails, to prevent further script errors
- cleaned up the outputs to help clarity within error messsages

Lessons learned:
- Write will make the file if it doesnt exist
- sys.exit(1) immediately ends the terminal session

Next steps:
- Introduce basic user input for file paths
- Validate user input before attempting file operations
- Handle invalid or missing input gracefully without crashing
- Begin separating configuration (paths, filenames) from transformation logic
