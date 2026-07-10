"""
Dictionary Comprehensions
Think of this as the dictionary version of list comprehensions.
Before we dive into analytics again, I want to make sure you understand the syntax.
"""
numbers = [1, 2, 3, 4, 5]
# Method 1
squares = {}

for number in numbers:
    squares = {number: number ** 2 for number in numbers}
print("Method 1", squares)

# method 2
squares = {}

for number in numbers:
    squares[number] = number ** 2
print("Method 2", squares)

"""
Step 1
What is the input?
List of dict.
key = "name"

Step 2
What should the output look like?
Hint: It should be a dictionary.
{"Samuel": 850}

Step 3
Key = "name"
Key = employee["name"]

Step 4
Value = "salary"
Value = employee["salary"]
"""