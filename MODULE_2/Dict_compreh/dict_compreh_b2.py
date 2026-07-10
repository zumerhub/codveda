"""
employees = [
    {"name": "Samuel", "salary": 850},
    {"name": "John", "salary": 700},
    {"name": "Mary", "salary": 750},
]
Question

Keep only employees whose salary is at least 750.

Output:

{
    "Samuel": 850,
    "Mary": 750
}
Step 1

Input = 
employee['name'] = employee['salary']
Step 2

Output = 
{
    "Samuel": 850,
    "Mary": 750
}

Step 3

Key = "name"

Step 4
Value = "salary"

Step 5

Write the dictionary comprehension.
"""

employees = [
    {"name": "Samuel", "salary": 850, "department": "IT" },
    {"name": "John", "salary": 700, "department": "HR"},
    {"name": "Mary", "salary": 750, "department": "Finance"},
]

analytics = {}

# method 1
for employee in employees:
    if  employee["salary"] >= 750:
        analytics[employee['name']] = { 
                                       "salary": employee["salary"], 
                                       "bonus": 100, 
                                       "department": employee["department"] 
                                    }
# OUTPUT: message
# analytics = {
#     employee['name'] : employee["salary"], 
#         "bonus": 100, 
#         "department": employee["department"] 
#     }
# ==========================================================     

        # analytics[employee["name"] + "_bonus" + " " ] = 100
        # analytics[employee["name"] + " " + "_department"] = employee["department"]
        # print(employee["name"])
        # print(employee["salary"])    
print(f"----1", analytics)


# method 2
analytics = { employee["name"]: { "salary": employee["salary"], "bonus": 100, "department": employee["department"] }
    for employee in employees
        if employee["salary"] >= 750              
}
print(f"----2", analytics)




# update the 
# for employee in employees:
#     if  employee["salary"] >= 750:
#         analytics[employee['name']] = employee["salary"]
#     #     employee['high_salary'] = True
#     # else:
#     #     analytics[employee['name']] = employee['salary']
#     #     employee['low_salary'] = False
     
# print(f"----1", analytics)
# # print(employee)
# print(f"----2", analytics)
