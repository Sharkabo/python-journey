# Task Description

**Scenario: The Corporate Org Chart**

You are analyzing the structure of a massive corporation. You have a root CEO, and everyone else reports to someone. You need to answer questions like: "How many total employees report to VP Smith?" (including *their* reports, and their reports' reports...).

**Your Goal:**
Build a **General Tree** structure (where a node can have *many* children, not just 2) and write a recursive function to count total descendants.

**Objectives:**
1.  Create a `EmployeeNode` class.
    - `name`: str
    - `children`: list[EmployeeNode] (initially empty).
    - `add_report(employee_node)` method to add a child.
2.  Build this hierarchy:
    - CEO
        - VP Sales
            - Manager A
                - Salesperson 1
                - Salesperson 2
            - Manager B
        - VP Eng
            - Lead Dev
                - Intern
3.  Implement a function `count_total_reports(node) -> int`:
    - It should return the number of people *under* this node (do not count the node itself, or do, just be consistent).
    - It MUST be recursive.

**Success Condition:**
Calling `count_total_reports(VP Sales)` should return 4 (Manager A, Sales 1, Sales 2, Manager B).
Calling `count_total_reports(CEO)` should return 7.
