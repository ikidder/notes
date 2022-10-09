# CAP Theorem

states that any distributed data store can provide only two of the following three guarantees:  

**Consistency**  
Every read receives the most recent write or an error.

**Availability**    
Every request receives a (non-error) response, without the guarantee that it contains the most recent write.

**Partition tolerance**  
The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.


## What it means
When a network partition failure happens, it must be decided whether to:
* cancel the operation and thus decrease the availability but ensure consistency 
* proceed with the operation and thus provide availability but risk inconsistency


https://en.wikipedia.org/wiki/CAP_theorem