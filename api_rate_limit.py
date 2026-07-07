"""Problem: API Rate Limit Analytics

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
Hint: Break problem into pieces

Ask yourself:

Which dictionaries do I need?

Maybe:

request counts
response totals
failed counts
slow endpoints

"""

# Solution
"""
API Rate Limit Analytics

Input:
1. Total requests per user
2. Average response time per user
3. User with highest number of failed requests

Failed requests = status code >= 400

4. Suspicious users
5. Slow endpoints

Given:
logs = [
    ("u1", "/predict", 120, 200),
    ("u2", "/login", 80, 200),
    ("u1", "/predict", 150, 500),
    ("u3", "/upload", 300, 200),
    ("u2", "/predict", 100, 429),
    ("u1", "/upload", 250, 200),
]
Log contains:
user_id, endpoint, response_time_ms, staus_code

"""

logs = [
    ("u1", "/predict", 120, 200),
    ("u2", "/login", 80, 200),
    ("u1", "/predict", 150, 500),
    ("u3", "/upload", 300, 200),
    ("u2", "/predict", 100, 429),
    ("u1", "/upload", 250, 200),
]
def api_limit_rate(logs):
    user = {}

    for user_id, endpoint, response_time, status_code in logs:
        user[user_id] = user.get(user_id, 0) + 1
        # dictionary[key] = dictionary.get(key, 0) + 1
    print(user)

    # 2. Average response time per user
    response_sum = {}

    for user_id, endpoint, response_time, status_code in logs:
        response_sum[user_id] = response_sum.get(user_id, 0) + response_time
    print("response time", response_sum)
    """therefore"""
    avg_response = {}

    for user_id in user:
        avg_response[user_id] = round(response_sum[user_id] / user[user_id], 2)

    print("avg_response", avg_response)
    
    # 3. User with highest number of failed requests

    # Failed requests = status code >= 400

    failed_count = {}

    for user_id, endpoint, response_time, status_code in logs:

        if status_code >= 400:
            failed_count[user_id]   = failed_count.get(user_id, 0) + 1 
    top_failed = max(failed_count, key=failed_count.get)
    print("failed_count", top_failed)

    # 4. Suspicious users
    # Any user with:
    # more than 2 failed requests
    # should be marked suspicious.
    # Example:
    # ["u1"]

    suspicious_user = []
    for user_id, total_failed in failed_count.items():
        if total_failed > 2:
            suspicious_user.append(user_id)
    print(total_failed)


    # 5. Slow endpoints
    # Any request with:
    # response_time_ms > 200
    # Track count per endpoint.

    endpoint_count = {}
    for user_id, endpoint, response_time, status_code in logs:
        endpoint_count[endpoint] = endpoint_count.get(endpoint, 0) + 1
    print(endpoint_count)

    endpoint_sum = {}

    for user_id, endpoint, response_time, status_code in logs:
        endpoint_sum[endpoint] = endpoint_sum.get(endpoint, 0) + response_time
    print(endpoint_sum)                        

    avg_endpoint = {}

    for endpoint in endpoint_count:
        avg_endpoint[endpoint] = round(endpoint_sum[endpoint]/ endpoint_count[endpoint], 2) 

    print(avg_endpoint)

    return {
        "requests_per_user": user,
        "avg_response_time": avg_response,
        "most_failed_user": top_failed,
        "suspicious_users": suspicious_user,
        "slow_endpoints": endpoint_count
    }

print(api_limit_rate(logs))