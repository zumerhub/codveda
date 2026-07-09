"""Problem: Conference Attendance Analytics

You are given attendance logs from a tech conference.

Each attendee checks in multiple times at different sessions.

Your task is to analyze the attendance data.

Each record contains:

(name, session_name, duration_minutes)

Example:

logs = [
    ("Samuel", "AI", 120),
    ("John", "Cloud", 90),
    ("Samuel", "ML", 100),
    ("Mary", "AI", 150),
    ("John", "DevOps", 80),
    ("Samuel", "LLM", 130),
]
Requirements

Write a Python program that returns:

1. Total attendance time per attendee

Example:

Samuel: 350
John: 170
Mary: 150
2. Attendee with highest total attendance time

Example:

Samuel
3. Average attendance time across all attendees

Example:

223.33
4. Any attendee with total time > 300 minutes should be marked:
VIP Attendee
Constraints
Number of logs can be between:
0 <= n <= 10000
Duration is positive integer.
Expected Output Example
{
    "attendance": {
        "Samuel": 350,
        "John": 170,
        "Mary": 150
    },
    "top_attendee": "Samuel",
    "average_time": 223.33,
    "vip": ["Samuel"]
}

"""

# Solution 

"""
Given 
(name, session_name, duration_minute)


"""
logs = [
    ("Samuel", "AI", 120),
    ("John", "Cloud", 90),
    ("Samuel", "ML", 100),
    ("Mary", "AI", 150),
    ("John", "DevOps", 80),
    ("Samuel", "LLM", 130),
]

attendance = {}

for name, session_name, duration in logs:
    attendance[name] = attendance.get(name, 0) + duration
print(name, duration)

# 2. max
top_attendee = max(attendance, key=attendance.get)
print(top_attendee)

# 3. average attendance
sum(attendance.values())
len(attendance)

aug_attendance = sum(attendance.values()) / len(attendance)
avg = round(aug_attendance, 2) 
print(avg)


VIP_attendance = []

for name, total in attendance.items():
    if total > 300:
        VIP_attendance.append(name)
print(VIP_attendance)