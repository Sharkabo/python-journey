# Task Description

**Scenario: The Undo/Redo System**

You are building a text editor. Every time the user types, you save their state. They hit Ctrl+Z to "Undo" (go back), and Ctrl+Y to "Redo" (go forward). A Singly Linked List can't do this efficiently because you can't go backwards from the current node. You need a Doubly Linked List.

**Your Goal:**
Implement a **Doubly Linked List** to track user states, allowing O(1) navigation in both directions.

**Objectives:**
1.  Create a `Node` class with `data` (string state like "Hello"), `next`, and `prev`.
2.  Create a `History` class.
    - `self.current`: Points to the current active state node.
3.  Implement `add_state(text)`:
    - Create a new node.
    - Link it *after* `self.current`.
    - Important: If `current` was in the middle of the history (after undoing), adding a new state should discarding all "future" (redo) nodes.
4.  Implement `undo()`: Move `current` to `current.prev` (if it exists). Return the text.
5.  Implement `redo()`: Move `current` to `current.next` (if it exists). Return the text.

**Success Condition:**
1.  Type "He". Add state.
2.  Type "Hel". Add state.
3.  Type "Hell". Add state.
4.  Undo -> Should return "Hel".
5.  Undo -> Should return "He".
6.  Redo -> Should return "Hel".
7.  Type "Help". Add state. (This should orphan "Hell" so you can't redo to it anymore).
8.  Verify the links are correct.
