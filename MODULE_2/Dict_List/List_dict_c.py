"""
📋 Question

Calculate the total salary paid by each department.

Notice carefully:

Before, we grouped by employee.

Now we are grouping by department.

Interview Framework
Step 1
What is the input?
List Dict

Step 2
What should the output look like?
Example:

{
    "IT": ?,
    "Finance": ?,
    "HR": ?
}
Fill in the values.
{
    "IT": 1750,
    "Finance": 1350,
    "HR": 1550
}

Step 3
What is the key? Be precise.

The key is "department"

Step 4
What is the transformation?

Choose one:
Count
Sum
Average
Group
Max
Min
Sort


Step 5
Write one dictionary entry only.

Example:

{
    "IT": ?
}
Step 6

Write the code.
"""

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
        "name": "Samuel",
        "department": "IT",
        "salary": 900
    },
    {
        "name": "Mary",
        "department": "HR",
        "salary": 750
    },
    {
        "name": "John",
        "department": "Finance",
        "salary": 650
    },
    {
        "name": "Mary",
        "department": "HR",
        "salary": 800
    }
]

analytics = {}

for employee in employees:
    if employee["department"] not in analytics:
        analytics[employee["department"]] = 0
    analytics[employee["department"]] += employee["salary"]
print(analytics)

"""{
    "IT": ["Samuel", "Samuel"],
    "Finance": ["John", "John"],
    "HR": ["Mary", "Mary"]
}

This is grouping by department, and it introduces a different update operation:

.append(...)
"""
analytics = {}
for employee in employees:
    if employee["department"] not in analytics:
        analytics[employee["department"]] = []
    analytics[employee["department"]].append(employee["name"])
print(f"---group", analytics)

"""
Now I'm going to make it a little more challenging.

Instead of storing one value...

We're going to store multiple statistics for each key.

For example:

{
    "IT": {
        "employees": ["Samuel", "Samuel"],
        "total_salary": 1750,
        "records": 2
    },
    "Finance": {
        "employees": ["John", "John"],
        "total_salary": 1350,
        "records": 2
    }
}
"""

# analytics = {}

# for employee in employees:
#     if employee["department"] not in analytics:
#         analytics[employee["department"]] = { "employees": [], "total_salary": 0, "records": 0,}
#     analytics[employee["department"]]["employees"].append(employee["name"])
#     analytics[employee["department"]]["total_salary"] += employee["salary"]
#     analytics[employee["department"]]["records"] += 1
    
   
# print(f"summary ",analytics) 


# clean method

analytics = {}

for employee in employees:
    department = employee["department"]
    name = employee["name"]
    salary = employee["salary"]

    if department not in analytics:
        analytics[department] = { "employees": [], "total_salary": 0, "records": 0,}
    analytics[department]["employees"].append(name)
    analytics[department]["total_salary"] += salary
    analytics[department]["records"] += 1
    
   
print(f"summary ",analytics) 