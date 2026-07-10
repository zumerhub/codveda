employees = [
    {"name": "Samuel", "salary": 850},
    {"name": "John", "salary": 700},
    {"name": "Mary", "salary": 750}
]

analytics = sorted(
        employees,
        key=lambda employee: employee["salary"])
print(analytics)