# Capstone Project: Task Management CLI Application

## 🎯 Project Overview

Build a complete **Task Management System** using all the Python skills you've learned from both phases. This project integrates:

- **Phase 1 Skills**: File I/O, dictionaries, lists, string formatting, error handling, control flow, list comprehensions
- **Phase 2 Skills**: OOP, type hints, decorators, context managers, custom exceptions, properties, magic methods, data structures

---

## 📋 Requirements

Create a command-line task management application with these features:

### Core Features
1. Create, read, update, and delete tasks
2. Set task priorities (High, Medium, Low)
3. Add categories/tags to tasks
4. Mark tasks as complete
5. Search and filter tasks
6. Persist data to JSON file
7. Display statistics and reports

### Technical Requirements
- Use **classes** for Task, TaskManager, and Priority
- Include **type hints** on all functions and methods
- Implement **custom exceptions** (TaskNotFoundError, InvalidTaskError)
- Use **decorators** for logging and input validation
- Use **context managers** for file operations
- Include **properties** with @property decorator
- Implement **magic methods** (__str__, __repr__, __len__)
- Use **list comprehensions** for filtering
- Proper **error handling** throughout

---

## 📝 Step-by-Step Implementation Guide

### Step 1: Define Custom Exceptions

Create custom exception classes:
- `TaskNotFoundError` - raised when a task ID doesn't exist
- `InvalidTaskError` - raised when task data is invalid
- `TaskStorageError` - raised when file operations fail

### Step 2: Create the Priority Enum

Create a `Priority` class that:
- Uses strings to represent priority levels: "HIGH", "MEDIUM", "LOW"
- Has a class method to validate priority values
- Has a method to get color codes for display (optional)

### Step 3: Create the Task Class

Implement a `Task` class with:

**Attributes:**
- `id: int` - unique task identifier
- `title: str` - task title
- `description: str` - detailed description
- `priority: str` - priority level
- `category: str` - task category
- `completed: bool` - completion status
- `created_at: str` - creation timestamp

**Methods:**
- `__init__()` - initialize task with type hints
- `__str__()` - return formatted task display
- `__repr__()` - return developer representation
- `to_dict()` - convert task to dictionary for JSON
- `from_dict()` (class method) - create task from dictionary
- `mark_complete()` - mark task as complete
- Property decorator for `is_overdue` (optional enhancement)

### Step 4: Create Decorators

Implement these decorators:

**@log_operation**
- Logs when operations are called
- Logs the operation name and timestamp
- Use this on all TaskManager methods

**@validate_task_id**
- Validates that task_id is a positive integer
- Raises InvalidTaskError if invalid
- Use this on methods that accept task_id

### Step 5: Create the TaskManager Class

Implement a `TaskManager` class with:

**Attributes:**
- `tasks: dict[int, Task]` - dictionary of tasks by ID
- `filename: str` - path to JSON storage file
- `next_id: int` - counter for new task IDs

**Core Methods:**
- `__init__(filename: str)` - initialize and load tasks
- `__len__()` - return number of tasks
- `add_task()` - create new task (use @log_operation)
- `get_task(task_id: int)` - retrieve task (use @validate_task_id)
- `update_task(task_id: int, **kwargs)` - update task fields
- `delete_task(task_id: int)` - remove task
- `list_all_tasks()` - return all tasks
- `mark_complete(task_id: int)` - mark task done

**Filter/Search Methods:**
- `filter_by_priority(priority: str)` - use list comprehension
- `filter_by_category(category: str)` - use list comprehension
- `filter_by_status(completed: bool)` - use list comprehension
- `search_tasks(keyword: str)` - search in title/description

**File Operations:**
- `save_tasks()` - save to JSON using context manager
- `load_tasks()` - load from JSON using context manager
- Handle FileNotFoundError for new files

**Statistics:**
- `get_statistics()` - return dict with task counts by priority/status
- `get_completion_rate()` - return percentage of completed tasks

### Step 6: Create the CLI Interface

Implement a `TaskCLI` class with:

**Methods:**
- `display_menu()` - show available options
- `run()` - main application loop
- `handle_create_task()` - get input and create task
- `handle_list_tasks()` - display all tasks
- `handle_update_task()` - update existing task
- `handle_delete_task()` - delete task
- `handle_search()` - search tasks
- `handle_filter()` - filter by priority/category/status
- `handle_statistics()` - display stats
- `handle_exit()` - save and exit

**Error Handling:**
- Wrap all operations in try/except
- Catch custom exceptions and display user-friendly messages
- Catch general exceptions for unexpected errors

### Step 7: Main Function

Create the main entry point:
- Initialize TaskManager with "tasks.json"
- Create TaskCLI instance
- Run the application
- Handle KeyboardInterrupt for graceful exit

---

## 🎨 Expected Output Examples

### Creating a Task
```
=== Task Manager ===
1. Create Task
2. List All Tasks
3. Update Task
4. Delete Task
5. Search Tasks
6. Filter Tasks
7. Mark Complete
8. Statistics
9. Exit

Choose option: 1

Enter task title: Complete Python Journey
Enter description: Finish all units in both phases
Enter priority (HIGH/MEDIUM/LOW): HIGH
Enter category: Learning

✓ Task created successfully! (ID: 1)
```

### Listing Tasks
```
=== All Tasks ===

[ID: 1] [HIGH] [INCOMPLETE] Complete Python Journey
Category: Learning
Created: 2026-02-12 04:00:00
Description: Finish all units in both phases

[ID: 2] [MEDIUM] [COMPLETE] ✓ Review OOP concepts
Category: Learning
Created: 2026-02-12 03:30:00
Description: Go through classes and inheritance

Total tasks: 2
```

### Statistics
```
=== Task Statistics ===

Total Tasks: 10
Completed: 6 (60.0%)
Incomplete: 4 (40.0%)

By Priority:
  HIGH: 2
  MEDIUM: 5
  LOW: 3

By Category:
  Learning: 4
  Work: 3
  Personal: 3
```

### Error Handling
```
Choose option: 3
Enter task ID to update: 999

✗ Error: Task with ID 999 not found.
```

---

## ✅ Completion Checklist

- [ ] All custom exceptions implemented
- [ ] Priority class with validation
- [ ] Task class with all required methods
- [ ] Task class has __str__ and __repr__
- [ ] Task.to_dict() and Task.from_dict() work correctly
- [ ] Decorators implemented (@log_operation, @validate_task_id)
- [ ] TaskManager class with all CRUD operations
- [ ] TaskManager uses context managers for file I/O
- [ ] Filter methods use list comprehensions
- [ ] Statistics methods implemented
- [ ] CLI interface with all menu options
- [ ] Proper error handling throughout
- [ ] Type hints on all functions/methods
- [ ] Tasks persist to JSON file
- [ ] Application handles invalid input gracefully
- [ ] All features tested and working

---

## 🚀 Bonus Challenges (Optional)

If you want to push further:

1. **Add due dates**: Include datetime handling and overdue task detection
2. **Color output**: Use ANSI codes to color-code priorities
3. **Task dependencies**: Allow tasks to depend on other tasks
4. **Export/Import**: Add CSV export/import functionality
5. **Recurring tasks**: Implement recurring task patterns
6. **Multiple users**: Add user authentication and separate task lists
7. **Search enhancements**: Implement regex-based search
8. **Undo/Redo**: Add command pattern for undo functionality

---

## 📌 Tips

- Start with the basic structure (exceptions, Task class)
- Test each component before moving to the next
- Use `if __name__ == "__main__":` to run your CLI
- Save frequently to avoid losing work
- Use descriptive variable names and add comments
- Don't forget type hints - they help catch bugs!

**Good luck! This project demonstrates everything you've learned. You've got this! 💪**
