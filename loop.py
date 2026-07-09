"""
write a loop function to iterate through a list of numbers and print each number multiplied by 2.
This combines:

loops
dictionaries
conditionals
problem solving
clean Python
"""  

# Question 
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

# Solution TO THE ABOVE EVALUation

"""
1. Total attendance 
2. Top attendee
3. Average attendee
4. VIP Attendee

code analysis would follow 
"""
# Input 
logs = [
    ("Samuel", "AI", 120),
    ("John", "Cloud", 90),
    ("Samuel", "ML", 100),
    ("Mary", "AI", 150),
    ("John", "DevOps", 80),
    ("Samuel", "LLM", 130),
]

"""
Dictionary method
"""
def analysis_attedance(logs):
    attendance = {}

    for name, session, duration in logs:
        attendance[name] = attendance.get(name, 0) + duration
        print(name, duration)

        print("======================================")
        print()

    # 2. Top attendee
    top_attendee = max(attendance, key=attendance.get)
    print("The top attendee is ", top_attendee)

    # 3. Average
    sum(attendance.values())
    len(attendance)
    average_time = sum(attendance.values())/ len(attendance)
    print("average_time :", average_time)

    # 4. VIP
    vip = []

    for name, total in attendance.items():
        if total > 300:
            vip.append(name)
            print ("vip :", vip)
        
    return {
         "attendance": attendance,
        "top_attendee": top_attendee,
        "average_time": round(average_time, 2),
        "vip": vip
    }

print(analysis_attedance(logs))