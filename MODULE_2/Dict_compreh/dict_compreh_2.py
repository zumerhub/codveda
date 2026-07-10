"""Mini Challenge (2 minutes)

Convert this for loop into a dictionary comprehension.

employees = [
    {"name": "Samuel", "salary": 850},
    {"name": "John", "salary": 700},
    {"name": "Mary", "salary": 750},
]

analytics = {}

for employee in employees:
    analytics[employee["name"]] = employee["salary"]

print(analytics)

Your task is to rewrite it using one line (excluding print).

💡 Hint: Start with the key and value, because you've become very good at identifying them.

I'm confident you can do this one without my help. Once you do, we'll move on to Advanced Sorting, which is another common interview topic.
"""
# Part A
# employees = [
#     {"name": "Samuel", "salary": 850},
#     {"name": "John", "salary": 700},
#     {"name": "Mary", "salary": 750},
# ]

# analytics = {}

# for employee in employees: 
#     analytics[employee["name"]] = employee["salary"]
# print(analytics)

# for employee in employees: 
#     name = ["name"]
#     salary = ["salary"]
    
#     if employee not in analytics:
#         analytics[employee] = analytics(employee, 0)
#     analytics[employee][name] += salary
        
# print(analytics)

# Part : B
employees = [
    {"name": "Samuel", "department": "IT"},
    {"name": "John", "department": "Finance"},
    {"name": "Mary", "department": "HR"},
]

"""# Write a dictionary comprehension that produces:

{
    "Samuel": "IT",
    "John": "Finance",
    "Mary": "HR"
}"""


analytics = {}

for employee in employees:
    analytics[employee['name']] = employee.get('department')
# or
    analytics[employee['name']] = employee["department"]
print(analytics)
# print(analytics)