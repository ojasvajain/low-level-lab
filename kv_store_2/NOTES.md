Design a Data Store to execute the following.

Part 1

Perform a READ, CREATE, UPDATE, DELETE functions

Create takes a String key and a String value - create(“key”, “val”) - return the stored value. If it exists, call update the function. (Hi Reader, if this feels like an normal over-write, wait until Part 3)

Read takes a String key - read(“key”) – Returns the stored value, else error, or friendly message.

Update takes a String key and String value – update(“key”, “val”) – returns the updated value, if it doesn’t exist, return and error or friendly message.

Delete takes a String key – delete(“key”) and deletes it from the store, else error, or friendly message

Example 1:

- read(“key1”) – returns “No Key associated”
- create(“key1”, “val1”) – returns “val1”
- read(“key1”) – returns “val1”
- update(“key1”, “val2”) – returns “val2”
- read(“key1”) – returns “val2”
- delete(“key1”) – returns “Delete Success”
- read(“key1”) – returns “No key associated”
Part 2

Enable transactions for your data store. A transaction starts with begin() and operations like READ, CREATE, UPDATE, DELETE can take place during this time. After these operation, the transaction is ended by either a commit() that commits everything permanently in the data store or rollback() that reverts everything that was performed during the transaction window. Notice that I highlighted the key-word everything.

Example 1:

- create(“key1”, “val1”)
- create(“key2”, “val2”)
- create(“key3”, “val3”)
- read(“key1”) – returns “val1”
- read(“key2”) – returns “val2”
- read(“key3”) – returns “val3”
- begin() – this begins a transaction
- create(“key3”, “val8”)
- read(“key3”) – returns val8
- create(“key5”, “val5”)
- read(“key5”) – returns val5
- update(“key5”, “val7”
- read(“key5”) – returns val7
- update(“key2”, “val7”
- read(“key2”) – returns val7
- update(“key2”, “val8”
- read(“key2”) – returns val8
- delete(“key1”)
- read(“key1”) – No Key Associated 
- commit() – this commits everything
After committing, you should still access the items in the data store with their update values.

- read(“key1”) – returns val8
- read(“key2”) – No Key Associated
- read(“key3”) – returns val8
Example 2: Disregard previous state of the Data Store

- create(“key1”, “val1”)
- create(“key2”, “val2”)
- create(“key3”, “val3”)
- read(“key1”) – returns “val1”
- read(“key2”) – returns “val2”
- read(“key3”) – returns “val3”

- begin() – this begins a transaction
- create(“key3”, “val8”)
- read(“key3”) – returns val8
- create(“key5”, “val5”)
- read(“key5”) – returns val5 
- update(“key5”, “val7”
- read(“key5”) – returns val7
- update(“key2”, “val7”
- read(“key2”) – returns val7
- update(“key2”, “val8”
- read(“key2”) – returns val8
- delete(“key1”)
- read(“key1”) – No Key Associated
- rollback() – this rolls back everything
- read(“key1”) – returns val1
- read(“key2”) – returns val2
- read(“key3”) – returns val3
- read(“key5”) – No Key Associated
Part 3

Make the transactions limited. In Part 2, commit() commits everything while rollback() rolls back everything. This part will ensure that you can only –

commit(t) - Commits only the first t transactions.
rollback(t) – rolls back  only the last t transactions.
For this part, Please note that only those operations that change the state of our data store are counted as transactions.

Example 1:

- create(“key1”, “val1”)
- create(“key2”, “val2”)
- create(“key3”, “val3”)
- read(“key1”) – returns “val1”
- read(“key2”) – returns “val2”
- read(“key3”) – returns “val3”
- begin() – this begins a transaction
- create(“key3”, “val8”)
- read(“key3”) – returns val8
- create(“key5”, “val5”)
- read(“key5”) – returns val5
- update(“key5”, “val7”
- read(“key5”) – returns val7
- update(“key2”, “val7”
- read(“key2”) – returns val7
- update(“key2”, “val8”
- read(“key2”) – returns val8
- delete(“key1”)
- read(“key1”) – No Key Associated
- commit(2) – this commits only the first two transactions
- read(“key1”) – returns val1
- read(“key2”) – returns val2
- read(“key3”) – returns val8
- read(“key5”) - returns val5
Example 2:

- create(“key1”, “val1”)
- create(“key2”, “val2”)
- create(“key3”, “val3”)
- read(“key1”) – returns “val1”
- read(“key2”) – returns “val2”
- read(“key3”) – returns “val3”
- begin() – this begins a transaction
- create(“key3”, “val8”)
- read(“key3”) – returns val8
- create(“key5”, “val5”)
- read(“key5”) – returns val5
- update(“key5”, “val7”
- read(“key5”) – returns val7
- update(“key2”, “val7”
- read(“key2”) – returns val7
- update(“key2”, “val8”
- read(“key2”) – returns val8
- delete(“key1”)
- read(“key1”) – No Key Associated
- rollback(2) – this rolls back only the last two transactions
- read(“key1”) – returns val1
- read(“key2”) – returns val7
- read(“key3”) – returns val8
- read(“key5”) - returns val7