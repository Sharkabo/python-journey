# Unit 09a: Iterators

## 1. What are Iterators?
An iterator is an object that allows you to loop through a collection one item at a time. When you use a `for` loop, Python automatically uses iterators behind the scenes.

**Syntax:**
```python
class IteratorClass:
    def __iter__(self):
        return self
    
    def __next__(self):
        # Return next item or raise StopIteration
        pass
```

**Example:**
```python
class Counter:
    def __init__(self, max_num):
        self.max_num = max_num
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num >= self.max_num:
            raise StopIteration
        self.num += 1
        return self.num

counter = Counter(5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5
```

---

## 2. Built-in Iterator Functions (Optional)
Use `iter()` and `next()` to work with iterators manually.

**Syntax:**
```python
iterator = iter(iterable)
item = next(iterator)
```

**Example:**
```python
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# Use default to avoid StopIteration error
print(next(iterator, "Done"))  # "Done"
```

---

## Spiral Learning Note
You've used `for` loops since Phase 1. Now you understand the iterator protocol behind them. Next you'll learn generators, an easier way to create iterators.
