# Design Goals
Goals that I've learned to prioritize based on experience.

## Minimize sources of truth
A source of truth, here, is a place where system behavior is defined.  

* Code - tells developers and the executing computers how the system should work
* Comments - tells developers *  * *
* Tests - tells developers *  *  * 
* Requirements - tells Product Owners, users, and developers * * * 
* Monitoring - describes how the system _did_ work
* Metrics - describes how the system _did_ work

Each of those sources of truth need to be created separately. That takes a lot of time and effort. And each of those sources need to be kept in sync with all the others. That takes even more time and effort. Particularly when different job roles and different teams have part ownership. Ever have a meeting with one team to decide on the wording of Section 3 Part A, and have a separate meeting to communicate that change to a different team?

Imagine we could write code, and some magic would happen, and:
1. Unit and Integration test would be automatically generated by the type system
2. Comments were automatically formatted and published
3. Monitoring constructs were automatically created based on the assertions made in the code
4. Metrics were published based on the objects created or modified during the execution

Some of that is already happening. And some of that is a research topic. 

The point is: Look for opportunities to use fewer sources of truth when it is possible.

## Make it easy on ourselves
Programmers are the first users of a system. We should design systems to make maintaining them as easy as possible. 
1. Enable quick changes
2. There's a good article on where to look for improvements. Look for "drudgery" in notes, and reference here.
3. Transparency. Make is easy to see what is happening in the system. More than just logging errors. Create dashboards that show not only alarms and metrics, but UI's that make it easy to say "yes, this thing went right".

If we just follow the business requirements, we will end up with a system that is difficult to understand, difficult to troubleshoot, and difficult to change. This sucks for us. And it impacts how we spend our time, and what we'll be able to deliver for the business in the future.