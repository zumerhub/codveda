employees = [
    {"name": "Samuel", "salary": 850},
    {"name": "John", "salary": 700},
    {"name": "Mary", "salary": 750},
    {"name": "David", "salary": 950},
    {"name": "Sarah", "salary": 820},
]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
    
)

top_3 = sorted_employees[:3]

print(top_3)