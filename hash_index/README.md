## Hash Based Database Index

Create a database storage engine from scratch. It should support: 

1. All CRUD operations
2. Creation of multiple tables
3. Compaction and Merging should be manually triggered
4. Rebuild Hash Table from Disk Contents (Crash Recovery)



Menu
1. Create table
    user specifies table name, columns and PK (all string)
2. Insert
3. Update
4. Delete
5. Perform compaction - should run in parallel. once complete user should get notified
should show statistics about size reduced, time taken
6. Rebuild hash table
7. Add index on column

Make it possible to plug your own implementation of hash table in future

Entities
1. Table
3. Segment (read max size from config)
2. Compaction Strategy
3. Menu

Simulate multiple reader and writer threads
