"""
Conference Attendance analytics
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
Given:
logs = [
    ("Samuel", "AI", 120),
    ("John", "Cloud", 90),
    ("Samuel", "ML", 100),
    ("Mary", "AI", 150),
    ("John", "DevOps", 80),
    ("Samuel", "LLM", 130),
]

1. Total attendance time per attendee
2. Attendee with highest tottal attendance time
3. Average attedance with across all attendees
4. VIP Attendee

record: name, session_name, duration_minutes
Input: 
"""

logs = [
        ("Samuel", "AI", 120),
        ("John", "Cloud", 90),
        ("Samuel", "ML", 100),
        ("Mary", "AI", 150),
        ("John", "DevOps", 80),
        ("Samuel", "LLM", 130),
    ]
def analytics_attendance(logs):
   
    # 1
    attendance = {}

    for name, session, duration in logs:
        attendance[name] = attendance.get(name, 0) + duration
        print(name, duration)
        print()

    # 2. Max attendee
    top_attendee = max(attendance, key=attendance.get)
    print(top_attendee)

    # 3. Average
    sum(attendance.values())
    len(attendance)
    average_time = sum(attendance.values()) / len(attendance) 
    avg = round(average_time, 2)
    print(avg)


    # 4. VIP attedanee
    vip = []
    for name, total in attendance.items():
        if total > 300:
            vip.append(name)

        print("vip",vip)
    return{
        "attendance": attendance,
        "top_attendance": top_attendee,
        "avg": avg,
        "vip": vip
    }
print("analytics_attendance", analytics_attendance(logs))