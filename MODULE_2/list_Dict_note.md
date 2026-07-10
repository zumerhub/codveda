analytics = {}

for record in data:
    key = ...
    value = ...

    if key not in analytics:
        analytics[key] = 0

    analytics[key] += value