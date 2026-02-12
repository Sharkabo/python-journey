# Task Description

**Scenario: The Browser History Manager**

You are building the "Back" and "Forward" button logic for a web browser. The history is a sequence of URLs. Users can visit new pages (append), but sometimes they might want to "inject" a page in the middle of history or "delete" a specific embarrassing URL from their history.

**Your Goal:**
Extend your Linked List to support **Insert** (at a specific position) and **Delete** (by value) operations.

**Objectives:**
1.  Reuse/Copy your `Node` and `LinkedList` structure.
2.  Implement `insert_after(target_val, new_val)`: Find the node with `target_val` and insert a new node *immediately after* it.
    - *Challenge:* You need to change the `next` pointer of the target node AND the `next` pointer of the new node. Order matters!
3.  Implement `delete(val)`: Find the node with `val` and remove it from the list.
    - *Challenge:* You need the *previous* node to change its `next` pointer to skip the deleted node.

**Success Condition:**
1.  Create list: `[Google] -> [GitHub] -> [Reddit]`.
2.  Insert `[StackOverflow]` after `[GitHub]`. List should look like: `Google -> GitHub -> StackOverflow -> Reddit`.
3.  Delete `[Reddit]`. Final list: `Google -> GitHub -> StackOverflow`.
4.  Print the final list to verify the links are correct.
