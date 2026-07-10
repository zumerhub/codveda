"""A list of dictionaries = a collection of records."""

"""⭐ Question 1 (Module 2)

Don't worry—we're starting simple.

Dataset
employees = [
    {
        "name": "Samuel",
        "department": "IT",
        "salary": 850
    },
    {
        "name": "John",
        "department": "Finance",
        "salary": 700
    },
    {
        "name": "Mary",
        "department": "HR",
        "salary": 750
    }
]
Your task

Without writing a loop yet, answer these questions.

Q1. What is the type of employees?
answer:
List of Dictionary

Q2. What is the type of:
employees[0]? 

answer: 
dict -> Dictionary
   {
        "name": "Samuel",
        "department": "IT",
        "salary": 850
    }

Q3. What will this return?
employees[0]["name"]

answer:
string -> 
"Samuel"

Q4. What will this return?
employees[2]["salary"]

answer:
integer -> 
 750

Q5. If we write:
for employee in employees: What is the type of employee?
Dictionary

🎯 Goal

Once you understand these five questions, you'll realize that the analytics patterns you've mastered don't change.

The only thing that changes is how you access the data.

For example:

Old tuple style:

for name, department, salary in employees:

New dictionary style:

for employee in employees:
    name = employee["name"]
    salary = employee["salary"]

The analytics logic (count, sum, group, aggregation) stays exactly the same.
"""