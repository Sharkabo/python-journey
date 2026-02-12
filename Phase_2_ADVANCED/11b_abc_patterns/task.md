# Task Description

**Scenario: The Swappable Database**

Your app currently saves users to a simple JSON file. But next week, you might migrate to a SQL database, or maybe a Cloud API. You don't want to rewrite your entire application logic every time the storage method changes. You need to decouple the "Business Logic" from the "Storage Logic".

**Your Goal:**
Implement the **Repository Pattern** using ABCs. This allows you to swap between a "File Storage" and a "Mock Storage" (for testing) without changing a single line of your main application code.

**Objectives:**
1.  Define an interface `UserRepository(ABC)` with methods:
    - `save(user: dict)`
    - `get(user_id: int) -> dict`
2.  Create a concrete class `FileUserRepository` that pretends to save to a file (print "Saving to file...").
3.  Create a concrete class `MockUserRepository` that saves to an in-memory dictionary (useful for fast tests).
4.  Write a "Business Logic" function `register_user(repo: UserRepository, name: str)`:
    - It should accept *any* repository that follows the interface.
    - It creates a user dict and calls `repo.save()`.

**Success Condition:**
You should be able to call `register_user` passing in a `FileUserRepository`, and then call it again passing in a `MockUserRepository`. The function works identically for both, proving your code is loosely coupled.
