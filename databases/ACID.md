# ACID

### Atomicity
guarantees that each transaction is treated as a single "unit", which either succeeds completely or fails completely

### Consistency
ensures that a transaction can only bring the database from one valid state to another, maintaining database invariants

### Isolation
ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially

### Durability
guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure. (i.e. saved to disk)



https://en.wikipedia.org/wiki/ACID