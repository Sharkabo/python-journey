# Unit 16: Capstone Project - Task Management System

## Project Overview
Build a complete Task Management System that applies all Phase 2 concepts: OOP, type hints, decorators, data structures, and algorithms.

**What You'll Build:**
A command-line task manager with task prioritization, categorization, deadline management, and file persistence.

---

## Core Features

**1. Task Management:**
- Create, update, delete, and list tasks
- Task properties: title, description, priority, category, deadline, status
- Status: TODO, IN_PROGRESS, COMPLETED
- Priority: LOW, MEDIUM, HIGH

**2. Organization:**
- Organize tasks into categories (Work, Personal, etc.)
- Filter by status, category, or priority
- Search by keyword

**3. Sorting and Filtering:**
- Sort by priority, deadline, or creation date
- Filter tasks
- Efficient search

**4. Persistence:**
- Save/load tasks from JSON file
- Auto-save on changes

---

## Technical Requirements

**Must Use:**

**1. OOP (Units 01-04):**
```python
class BaseEntity:
    # Base class with common properties

class Task(BaseEntity):
    # Properties with validation
    # Type hints on methods
```

**2. Type Hints (Unit 05):**
```python
from typing import Optional, List
from datetime import datetime

def create_task(
    title: str,
    priority: str,
    deadline: Optional[datetime] = None
) -> Task:
    pass
```

**3. Decorators (Unit 07):**
```python
@log_operation
@validate_input
def add_task(self, task: Task) -> None:
    pass
```

**4. Data Structures & Algorithms (Units 13-15):**
```python
# Efficient organization and searching
# O(n log n) sorting
```

---

## Suggested Architecture

```
capstone_project/
├── models/
│   ├── task.py
│   └── enums.py
├── managers/
│   ├── task_manager.py
│   └── file_manager.py
├── utils/
│   ├── decorators.py
│   └── validators.py
└── main.py
```

---

## Implementation Phases

**Phase 1:** Core models (Task, BaseEntity) (30%)
**Phase 2:** Manager classes with CRUD (30%)
**Phase 3:** Algorithms (sorting, filtering, search) (20%)
**Phase 4:** User interface menu (20%)

---

## Spiral Learning Note

This project integrates all Phase 2 concepts:
- Units 01-04: OOP
- Unit 05: Type hints
- Unit 07: Decorators
- Units 10-12: Context managers, ABC, exceptions
- Units 13-15: Data structures and algorithms

This prepares you for FastAPI in Phase 3. The architecture mirrors real web APIs.
