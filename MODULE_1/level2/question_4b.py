"""🏆 Bonus Report Challenge (Final Test)
Dataset
employees = [
    ("Samuel", "IT", 850),
    ("John", "Finance", 700),
    ("Samuel", "IT", 900),
    ("Mary", "HR", 750),
    ("John", "Finance", 650),
    ("Mary", "HR", 800),
]

Each tuple contains:

(employee_name, department, salary)
📋 Question

Create a report for each employee that contains:

{
    "Samuel": {
        "records": 2,
        "total_salary": 1750
    },
    "John": {
        "records": 2,
        "total_salary": 1350
    },
    "Mary": {
        "records": 2,
        "total_salary": 1550
    }
}
🚫 Interview Rules

Don't jump to the code.

Follow the six-step process.

Step 1

What is the input?

Step 2

What should the output look like?

Step 3

What is the key?

Step 4

What transformations are required?

(There are two transformations in this question.)

Step 5

Write one dictionary entry only.

Example:

{
    "Samuel": ?
}
Step 6

Write the code.

⭐ No Hints This Time

This is your graduation test for Module 1.

If you complete it correctly:

I won't help.
I won't give hints.
I'll grade it exactly like a software engineering interview.

I genuinely want to see whether you can solve it independently from start to finish.

Good luck, Engineer. 🚀💪
"""

employees = [
    ("Samuel", "IT", 850),
    ("John", "Finance", 700),
    ("Samuel", "IT", 900),
    ("Mary", "HR", 750),
    ("John", "Finance", 650),
    ("Mary", "HR", 800),
]

reports = {}

for employee_name, department, salary in employees:
    if employee_name not in reports:
        reports[employee_name] = {"records": 0, "total_salary": 0}
        
    reports[employee_name]["records"] += 1
    reports[employee_name]["total_salary"] += salary
print(reports) 

"""
Answer to the Logic questions

Step 1
What is the input?
List tuple 
employee_name, department, salary

Step 2
What should the output look like?
{"samuel": {'records': 2, 'total_salary':1750}}

Step 3
What is the key?
employee_name

Step 4
What transformations are required?
(There are two transformations in this question.)

"COUNT" the number of time the "key= employee_name" appears and "SUM" the "value=salary"


Step 5
Write one dictionary entry only.
Example:
{
    "Samuel": ?
}
Answer
{
    "Samuel": {"recods":2, "total_spent": 1750}?
}

Step 6

Write the code."""