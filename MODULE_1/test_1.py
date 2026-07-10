"""
Now we move from drills → realistic problem solving.

This one combines everything you learned:

loop
iteration
counting
summing
conditions
max
Problem — API Request Analytics

Input:

logs = [
    ("u1", 200, 120),
    ("u2", 500, 300),
    ("u1", 200, 100),
    ("u3", 404, 250),
    ("u2", 200, 150),
]

Each tuple means:

(user_id, status_code, response_time)

Example:

("u1", 200, 120)

means:

user_id = u1
status_code = 200
response_time = 120
Tasks
1. Count requests per user

Expected:

{
    "u1": 2,
    "u2": 2,
    "u3": 1
}
2. Sum response time per user

Expected:

{
    "u1": 220,
    "u2": 450,
    "u3": 250
}
3. Count failed requests per user

Failed request means:

status_code >= 400

Expected:

{
    "u2": 1,
    "u3": 1
}
4. Find user with highest requests

Use:

max(..., key=...get)

We solve one step at a time.

Start with Step 1 only.

Count requests per user.
"""


logs = [
    ("u1", 200, 120),
    ("u2", 500, 300),
    ("u1", 200, 100),
    ("u3", 404, 250),
    ("u2", 200, 150),
]

count = {}

for user_id, status_code, respons_time in logs:
    count[user_id] = count.get(user_id, 0) + 1
print(count)

# 2. Sum response time per user

check_user = {}
for user_id, status_code, respons_time in logs:
    check_user[user_id] = check_user.get(user_id, 0) + respons_time
print(check_user)

# 3. Count failed requests per user
# status_code >= 400

failed_request = {}
for user_id, status_code, respons_time in logs:
    if status_code >= 400:
        failed_request[user_id] = failed_request.get(user_id, 0) + 1
print(failed_request) 

# 4.
top_user = max(count, key=count.get)
print(top_user)
