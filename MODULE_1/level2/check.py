"""Question

How many days did each employee attend work?

Step 1

What is the input?

Step 2

What should the output look like?

Step 3

What is the key?

Step 4

What is the transformation?

Choose one:

Count
Sum
Average
Max
Min
Sort
Group
Step 5

Write one dictionary entry only.

Example:

{
    "Samuel": ?
}
Step 6

Write the code.
"""

attendance = [
    ("Samuel", "Monday"),
    ("John", "Monday"),
    ("Samuel", "Tuesday"),
    ("Mary", "Monday"),
    ("John", "Wednesday"),
    ("Mary", "Friday"),
]

analytics = {}

for employee_name, days in attendance:
    if employee_name not in analytics:
        analytics[employee_name] = 0
    analytics[employee_name] += 1
print(analytics)

# method 2 

analytics = {}

for employee_name, day in attendance:
    analytics[employee_name] = analytics.get(employee_name, 0) + 1
print(f"---", analytics)