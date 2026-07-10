"""Question 4 — Aggregation (Real-World Analytics)

This is where everything you've learned comes together.

Dataset:

sales = [
    ("Samuel", "Laptop", 800),
    ("John", "Mouse", 25),
    ("Samuel", "Keyboard", 50),
    ("Mary", "Laptop", 800),
    ("John", "Monitor", 200),
    ("Mary", "Mouse", 25),
]
Question

For each customer, produce this report:

{
    "Samuel": {
        "orders": 2,
        "total_spent": 850
    },
    "John": {
        "orders": 2,
        "total_spent": 225
    },
    "Mary": {
        "orders": 2,
        "total_spent": 825
    }
}

This question combines two patterns you've already mastered:

Count → orders
Sum → total_spent

You're not learning a new operation here. You're learning how to combine multiple operations into a single nested dictionary.

Bootcamp Status: 🚀 Question 4 is now live.
"""

sales = [
    ("Samuel", "Laptop", 800),
    ("John", "Mouse", 25),
    ("Samuel", "Keyboard", 50),
    ("Mary", "Laptop", 800),
    ("John", "Monitor", 200),
    ("Mary", "Mouse", 25),
]

analytics = {}
"""
Using: 
Dictionary of Dictionaries
data[key]["orders"] += 1
"""
for customer_name, product_name, price in sales:
    if customer_name not in analytics:
        analytics[customer_name] = {"order": 0, "total_spent": 0}
    analytics[customer_name]["order"] += 1 
    analytics[customer_name]["total_spent"] += price
print(analytics)