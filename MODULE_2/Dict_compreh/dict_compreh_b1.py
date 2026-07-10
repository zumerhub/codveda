"""
🏆 Dictionary Comprehension Drill 1 (Basic)
Dataset
employees = [
    {"name": "Samuel", "salary": 850},
    {"name": "John", "salary": 700},
    {"name": "Mary", "salary": 750},
]
Question

Create a dictionary where:

Key = employee name
Value = salary
Step 1

Input = for employee in employees
key = "name"  
value = "salary"

Step 2

Output = {"samuel": 850}

Step 3

Key = "Samuel"

Step 4

Value = 850

Step 5

Write the dictionary comprehension.
"""

employees = [
    {"name": "Samuel", "salary": 850},
    {"name": "John", "salary": 700},
    {"name": "Mary", "salary": 750},
]

analytics = {}

for employee in employees:
    analytics[employee['name']] = employee["salary"]
print(analytics)