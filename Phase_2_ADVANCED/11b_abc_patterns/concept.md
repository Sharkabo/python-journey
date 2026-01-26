# Unit 11b: ABC Patterns

## 1. Repository Pattern
The repository pattern uses ABCs to ensure all data storage implementations follow the same interface.

**Syntax:**
```python
from abc import ABC, abstractmethod

class RepositoryABC(ABC):
    @abstractmethod
    def save(self, data):
        pass
    
    @abstractmethod
    def get(self, id):
        pass
```

**Example:**
```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(self, data):
        pass
    
    @abstractmethod
    def get(self, id):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

class SQLRepository(Repository):
    def save(self, data):
        # Save to SQL database
        print(f"Saving to SQL: {data}")
    
    def get(self, id):
        # Get from SQL database
        return f"Data for ID {id}"
    
    def delete(self, id):
        # Delete from SQL database
        print(f"Deleting ID {id}")

repo = SQLRepository()
repo.save({"name": "Alice"})
print(repo.get(1))
```

---

## Spiral Learning Note
Unit 11a taught ABC basics. Now you use them in design patterns like Repository. Ensures consistency across different implementations. Used in frameworks and large projects.
