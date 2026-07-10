
"""
Step 1
What is the input?
list of dictionary
employee in employees

Step 2
What should the output look like?
Dictionary


Step 3
What is the key?
 {
        "Samuel": { "salary": 850 }
    }

Step 4
What is the transformation?
Choose one:
Sum


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
    "Samuel": ?
}
Step 6

Write the code.
Calculate the total salary paid to each employee.
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
    }
]

# analytics = {}

# for employee in employees:
#     if employee["name"] not in analytics:
#         analytics[employee["name"]] = 0
#     analytics[employee["name"]] +=  employee["salary"]

     
# print(analytics) 

# Method 2
analytics = {}

for employee in employees:
    analytics[employee["name"]] = (
        analytics.get(employee["name"], 0) + employee["salary"])
print(analytics)