# Task Description

**Scenario: The Real-Time Leaderboard**

You are running a game server. Thousands of scores come in every minute. You need to store them in a way that lets you quickly search if a specific score exists, or find where a new score fits. A regular list is too slow (`O(n)` search). A Binary Search Tree (BST) allows `O(log n)` average search and insertion.

**Your Goal:**
Implement a **Binary Search Tree** that automatically places lower scores to the left and higher scores to the right.

**Objectives:**
1.  Create `Node` with `score` (int), `left`, `right`.
2.  Create `LeaderboardBST` class.
3.  Implement `insert(score)`:
    - If tree is empty, new node is root.
    - If not empty, traverse down:
        - Go LEFT if `score < current.score`.
        - Go RIGHT if `score >= current.score`.
        - Place the new node when you hit a `None` spot.
4.  Implement `exists(score) -> bool`:
    - Traverse the tree efficiently (binary search logic) to find if a score is present.

**Success Condition:**
Insert scores: [50, 30, 70, 20, 40, 60, 80].
Manually verify the structure:
- Root is 50.
- Root.left is 30.
- Root.right is 70.
- Root.left.left is 20.
Calling `exists(40)` should return True. Calling `exists(99)` should return False.
