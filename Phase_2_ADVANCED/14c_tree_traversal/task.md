# Task Description

**Scenario: The Syntax Tree Evaluator**

Compilers don't read code line-by-line; they turn it into an "Abstract Syntax Tree". For example, the math expression `(5 + 3) * 2` becomes a tree where `*` is the root, `+` is the left child, and `2` is the right child. To calculate the answer, you must evaluate the children *before* the parent (Postorder Traversal).

**Your Goal:**
Build a simple Expression Tree and write a `postorder_evaluate` function to solve it.

**Objectives:**
1.  Create a `Node` that can hold a value (int) OR an operator (str `+`, `*`).
2.  Manually build the tree for `(5 + 3) * 2`:
    - Root: `*`
    - Left: `+` (Left: 5, Right: 3)
    - Right: 2
3.  Implement `evaluate(node) -> int`:
    - **Base Case:** If node is a number (leaf), return it.
    - **Recursive Step:**
        - `left_val = evaluate(node.left)`
        - `right_val = evaluate(node.right)`
        - Apply the operator (`*` or `+`) to `left_val` and `right_val` and return result.

**Success Condition:**
Calling `evaluate(root)` should return 16 (`(5+3)*2` = `8*2` = 16).
This proves you can process a tree from the bottom up!
