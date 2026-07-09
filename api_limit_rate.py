"""
Problem: API Rate Limit Analytics

You are given API request logs from a SaaS platform.

Each log contains:

(user_id, endpoint, response_time_ms, status_code)

Example:

logs = [
    ("u1", "/predict", 120, 200),
    ("u2", "/login", 80, 200),
    ("u1", "/predict", 150, 500),
    ("u3", "/upload", 300, 200),
    ("u2", "/predict", 100, 429),
    ("u1", "/upload", 250, 200),
]
Requirements

Write a function:

def analyze_api_logs(logs):

Return:

1) Total requests per user

Example:

{
    "u1": 3,
    "u2": 2,
    "u3": 1
}
2) Average response time per user

Example:

{
    "u1": 173.33,
    "u2": 90.0,
    "u3": 300.0
}
3) User with highest number of failed requests

Failed requests = status code >= 400

Example:

u1

Because:

u1 → one failed (500)
u2 → one failed (429)

If tie, return any.

4) Suspicious users

Any user with:

more than 2 failed requests

should be marked suspicious.

Example:

["u1"]
5) Slow endpoints

Any request with:

response_time_ms > 200

Track count per endpoint.

Example:

{
    "/upload": 2
}
Expected Output Format
{
    "requests_per_user": {...},
    "avg_response_time": {...},
    "most_failed_user": "u1",
    "suspicious_users": [...],
    "slow_endpoints": {...}
}
Constraints
0 <= n <= 10000
"""

# (user_id, endpoint, response_time_ms, status_code)

logs = [
    ("u1", "/predict", 120, 200),
    ("u2", "/login", 80, 200),
    ("u1", "/predict", 150, 500),
    ("u3", "/upload", 300, 200),
    ("u2", "/predict", 100, 429),
    ("u1", "/upload", 250, 200),
]

request_per_user = {}

# 1) Total requests per user

for user_id, endpoint, respons_time_ms, status_code in logs:
    request_per_user[user_id] = request_per_user.get(user_id, 0) + 1
print(request_per_user)

# 2) Average response time per user
response_times = {}
request_counts = {}

for user_id, endpoint, respons_time_ms, status_code in logs:
    response_times[user_id] = response_times.get(user_id, 0) + respons_time_ms
    request_counts[user_id] = request_counts.get(user_id, 0) + 1

# print(response_times, request_counts)

avg_response_time = {
    user: round((response_times[user])/ request_per_user[user],2)
    for user in response_times
}
print(avg_response_time)

# 3) User with highest number of failed requests
failed_request = {}

for user_id, endpoint, respons_time_ms, status_code in logs:
    if status_code >= 400:
        failed_request[user_id] = failed_request.get(user_id, 0) + 1

if failed_request:
    most_failed_user = max(failed_request, key=failed_request.get)
else:
    most_failed_user = None

print(most_failed_user)

