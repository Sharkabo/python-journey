# Task Description

**Scenario: The Financial Data Pipeline**

You are a Junior Data Engineer at a fintech startup. Your boss just dumped a raw list of transaction dictionaries on your desk. Each transaction has an `id`, `amount`, `type` ("credit" or "debit"), and `status` ("pending" or "completed").

"I need a clean list of all *completed debit* transactions, sorted by amount (highest first)," she says. "And convert the amounts to strings with a '$' sign. DO NOT write a loop for this. Use functional programming."

**Your Goal:**
Build a data processing pipeline using `filter()`, `sorted()`, and `map()` combined with `lambda` functions.

**Objectives:**
1.  Define a list of raw transaction dictionaries (at least 5 items with mixed types and statuses).
2.  **Filter:** Create a new list `debits` containing only transactions where `type == "debit"` AND `status == "completed"`. Use `filter()` and a `lambda`.
3.  **Sort:** Sort the `debits` list by `amount` in *descending* order (largest first). Use `sorted()` and a `lambda` key.
4.  **Map:** Create a final list of strings `formatted_amounts` that formats the amount like `"$100.50"`. Use `map()` and a `lambda`.
5.  Print the final list.

**Success Condition:**
Your code should output a clean list of strings like `['$500.00', '$120.50', '$25.00']` without using a single `for` or `while` loop for the logic.
