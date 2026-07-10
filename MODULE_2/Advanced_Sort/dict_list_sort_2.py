"""🎯 Mini Challenge (No code)

This one is for your reasoning skills.

Given:

employees = [
    {"name": "Samuel", "salary": 850, "department": "IT"},
    {"name": "John", "salary": 700, "department": "HR"},
    {"name": "Mary", "salary": 750, "department": "Finance"},
    {"name": "David", "salary": 950, "department": "IT"},
]

Answer these:

Input?
If I say "Top 2 highest-paid employees," what should the output look like?
Which field should Python compare?
Should the sort be ascending or descending?

This introduces the next topic: Top N, which is one of the most common
interview and analytics patterns. I think you'll find it much easier now because it builds directly on everything you've already learned.
"""

employees = [
    {"name": "Samuel", "salary": 850},
    {"name": "John", "salary": 700},
    {"name": "Mary", "salary": 750},
    {"name": "David", "salary": 950},
    {"name": "Sarah", "salary": 820}
]
# descending
sorted_employee = sorted( 
                         employees,
                         key=lambda employee: employee["salary"],
                         reverse=True)
print(sorted_employee)

