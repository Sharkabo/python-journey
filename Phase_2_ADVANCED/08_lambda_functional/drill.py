# Drills - Lambda and Functional Programming
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a lambda that adds 10 to a number
def add_10(num):
    return num + 10
add_lambda = lambda num: num + 10

# Drill 2: Use map() to square all numbers in [1, 2, 3, 4, 5]
list_num: list[int] = [1, 2, 3, 4, 5]
squared = list(map(lambda num: num ** 2, list_num))

# Drill 3: Use filter() to get only positive numbers from [-2, -1, 0, 1, 2]
list_mix_num: list[int] = [-2, -1, 0, 1, 2]
result: list[int] = list(filter(lambda x: x > 0, list_mix_num))

# Drill 4: Use lambda with sorted() to sort ['apple', 'kiwi', 'banana'] by length
fruit: list[str] = ['apple', 'kiwi', 'banana']
sorted_fruit = sorted(fruit, key = lambda x:(len(x), x))

# Drill 5: Use map() to convert ['alice', 'bob'] to uppercase
names: list[str] = ['alice', 'bob']
upper_names = map(lambda name: name.upper(), names)

# Drill 6: Use filter() to get students with grade >= 80 from a list of dicts
grade: dict[str, int] = {"Alice": 90, "Bob": 70, "Cathy": 45}
better_grade: dict[str, int] = dict(filter(lambda x: x[1] > 80, grade.items()))

# Drill 7: Use sorted() with lambda to sort tuples by the second element
data = [(5, 10), (1, 2), (8, 5)]
tuple_result = sorted(data, key = lambda x: x[1])

# Drill 8: Use reduce() to find the product of [1, 2, 3, 4, 5]
from functools import reduce
numbers: list[int] = [1, 2, 3, 4, 5]
product: int = reduce(lambda x, y: x*y, numbers)

# Drill 9: Chain map and filter: double even numbers only from [1, 2, 3, 4, 5, 6]
num_todo: list = [1, 2, 3, 4, 5, 6]
result_lambda = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, num_todo)))

# Drill 10: Rewrite a map/filter operation as a list comprehension
result_comprehension = [x * 2 for x in num_todo if x % 2 == 0]