"""Drill 3 adds one new thing:

if condition:

That means:

loop through data
count
apply condition
Problem: Late Employee Tracker

Input:

records = [
    ("Samuel", 8),
    ("John", 10),
    ("Mary", 7),
    ("Samuel", 11),
    ("John", 9)
]

Meaning:

(employee_name, arrival_time)

Rule:

Arrival after 9 = late

Examples:

8 → not late
9 → not late
10 → late
11 → late

Task:

Find:

1. Total arrivals per employee

Expected structure:

{
    "Samuel": ?,
    "John": ?,
    "Mary": ?
}
2. Late count per employee

Expected structure:

{
    "Samuel": ?,
    "John": ?
}

Only count when:

arrival_time > 9

3. Find employee with highest late count.

Expected:

top_late = "John" or "Samuel"
Start with framework.

Tell me:

Input
Output
Data structure
Pattern

Then 
write step 1 only:
Total arrivals per employee."""

# Solution
records = [
    ("Samuel", 8),
    ("John", 10),
    ("Mary", 7),
    ("Samuel", 11),
    ("John", 9)
]

"""Given:
loop through data
count
apply condition
Problem: Late Employee Tracker
(employee_name, arrival_time)
1. Total arrivals per employee
"""

count = {}

for employee_name, arrival_time in records:  # Dictionary counting
    count[employee_name] = count.get(employee_name, 0) + 1
print(count)
        
# 2. Late count per employee
"""
Only count when:

arrival_time > 9
"""


late_count = {}

for employee_name, arrival_time in records:
    if arrival_time > 9:  # Condition checks
        late_count[employee_name] = late_count.get(employee_name, 0) + 1
print(late_count)

"""
# 3. Find employee with highest late count.

Expected:

top_late = "John" or "Samuel"
"""
top_late = max(late_count, key=late_count.get)
print(top_late)

