# Unit 04: Magic Methods (Dunder Methods)

## 1. What are Magic Methods?
Magic methods (dunder methods - double underscore) are special methods that Python calls automatically in certain situations. They allow you to customize how your objects behave.

**Syntax:**
```python
class ClassName:
    def __str__(self):
        return "String representation"
    
    def __eq__(self, other):
        return self.value == other.value
```

**Example:**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("Clean Code", "Robert Martin")
print(book)          # Clean Code by Robert Martin
print(repr(book))    # Book('Clean Code', 'Robert Martin')
```

---

## 2. Common Magic Methods (Optional)
Make your objects behave like built-in types.

**Syntax:**
```python
def __len__(self):     # len(obj)
def __getitem__(self, index):  # obj[index]
def __add__(self, other):      # obj + other
def __eq__(self, other):       # obj == other
```

**Example:**
```python
class Playlist:
    def __init__(self):
        self.songs = []
    
    def __len__(self):
        return len(self.songs)
    
    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist()
playlist.songs = ["Song1", "Song2"]
print(len(playlist))    # 2
print(playlist[0])      # Song1
```

---

## Spiral Learning Note
You learned `__init__` in Unit 01. Magic methods extend that for customization. Next you'll learn type hints and advanced patterns.
