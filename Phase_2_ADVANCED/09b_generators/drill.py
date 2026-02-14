# Drills - Generators
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a generator function that yields numbers 1 to n
def count_up(max_num: int):
    num: int = 1
    while num < max_num:
        yield num
        num += 1

# Drill 2: Create a Fibonacci generator using yield
def fibonacci(limit: int):
    num_a = 0
    num_b = 1
    for i in range(limit):
        yield num_a
        num_a, num_b = num_a, (num_a + num_b)

# Drill 3: Create a generator for reading large files line by line
from typing import Any
def readfile(filename: str)-> Any:
    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            yield line.strip()

# Drill 4: Create a generator expression for squares
def squares_gen(num: int)-> Any:
    return (x ** 2 for x in range(num))

# Drill 5: Create an infinite generator
from itertools import count

def infinite_gen(start: int = 0)-> Any:
    return count(start)

# Drill 6: Create a generator that filters odd numbers
def odd_filter_gen(input_num: int)-> Any:
    return (x for x in range(input_num) if x % 2 != 0)

# Drill 7: Use next() on a generator
def simple_gen():
    yield 'A'
    yield 'B'
    yield 'C'

text_cube = simple_gen()
print(next(text_cube))
print(next(text_cube))

# Drill 8: Create a generator for prime numbers
import math

def is_prime(num: int)-> bool:
    if num < 2:return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def prime_gen()-> Any:
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1