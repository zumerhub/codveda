"""
Drill 1 (Warmup — Easy)

Problem:

You are given a list of employees entering a company building.

employees = [
    "Samuel",
    "John",
    "Samuel",
    "Mary",
    "John",
    "Samuel"
]

Task:
Count how many times each employee entered.

Expected output:

{
    "Samuel": 3,
    "John": 2,
    "Mary": 1
}

Follow the framework.

Answer these first:

1. Input?
2. Output?
3. Data structure?
4. Pattern? (count / sum / filter / max)
"""

# Solution
"""
1. Input: List of employee names
2. Output: Count of how many times each employee appears
{
    "Samuel": 3,
    "John": 2,
    "Mary": 1
}
3. Data structure: Dictionary Method
4. Pattern: Counting
"""

check_iterations = [ "A", "B", "A"]


iteration = {}

# print("Before loop:", iteration)
# print("------------------------")

for char_name in check_iterations:
    # print("Current employee: ", char_name)
    old_value = iteration.get(char_name, 0)
    # print("Old value", old_value)

    new_value = old_value + 1
    # print("New value:", new_value)
    # print()
    
    iteration[char_name] = new_value
  
    # print("Updated iteration:", iteration)
    # print("-----")



employees = [ 
   "Samuel",
    "John",
    "Samuel",
    "Mary",
    "John",
    "Samuel"
]

attendance = {}

for employee_name in employees:
    attendance[employee_name] = attendance.get(employee_name, 0) + 1
     # dict[key] = dick.get(key, 0) + 1 
# print(attendance)

# =================================== end 1=======================
"""
You’re ready for Drill 2 now:

Count sessions attended by employees using tuples like:

records = [
    ("Samuel", "Morning"),
    ("John", "Evening"),
    ("Samuel", "Afternoon")
]

Goal:

{'Samuel': 2, 'John': 1}

"""
records = [
    ("Samuel", "Morning"),
    ("John", "Evening"),
    ("Samuel", "Afternoon")
]

attendance_record = {}

for employee_name, sessions in records:
    attendance_record[employee_name] = attendance_record.get(employee_name, 0) + 1
print(attendance_record)
