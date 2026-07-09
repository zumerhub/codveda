"""Problem: E-commerce Order Analytics

You are given a list of customer orders.

Each order contains:

(customer_name, product_name, quantity, price_per_unit)

Example:

orders = [
    ("Samuel", "Laptop", 1, 800),
    ("John", "Mouse", 2, 25),
    ("Samuel", "Keyboard", 1, 50),
    ("Mary", "Laptop", 1, 800),
    ("John", "Monitor", 1, 200),
]
Requirements

Write a Python function:

def analyze_orders(orders):

Return:

1) Total money spent per customer

Example:

{
    "Samuel": 850,
    "John": 250,
    "Mary": 800
}

Because:

Samuel = 800 + 50 = 850
John = (2×25) + 200 = 250
2) Customer who spent the most

Example:

Samuel
3) Average spending across customers

Example:

633.33
4) VIP customers

Anyone spending more than:

500

should be marked VIP.

Example:

["Samuel", "Mary"]
Constraints
0 <= n <= 10000Problem: E-commerce Order Analytics

You are given a list of customer orders.

Each order contains:

(customer_name, product_name, quantity, price_per_unit)

Example:

orders = [
    ("Samuel", "Laptop", 1, 800),
    ("John", "Mouse", 2, 25),
    ("Samuel", "Keyboard", 1, 50),
    ("Mary", "Laptop", 1, 800),
    ("John", "Monitor", 1, 200),
]
Requirements

Write a Python function:

def analyze_orders(orders):

Return:

1) Total money spent per customer

Example:

{
    "Samuel": 850,
    "John": 250,
    "Mary": 800
}

Because:

Samuel = 800 + 50 = 850
John = (2×25) + 200 = 250
2) Customer who spent the most

Example:

Samuel
3) Average spending across customers

Example:

633.33
4) VIP customers

Anyone spending more than:

500

should be marked VIP.

Example:

["Samuel", "Mary"]
Constraints
0 <= n <= 10000
Expected Output
{
    "customer_spending": {
        "Samuel": 850,
        "John": 250,
        "Mary": 800
    },
    "top_customer": "Samuel",
    "average_spending": 633.33,
    "vip_customers": ["Samuel", "Mary"]
}
Expected Output
{
    "customer_spending": {
        "Samuel": 850,
        "John": 250,
        "Mary": 800
    },
    "top_customer": "Samuel",
    "average_spending": 633.33,
    "average_spending": ["Samuel", "Mary"]
}
"""


# Solution 

import unittest
orders = [
    ("Samuel", "Laptop", 1, 800),
    ("John", "Mouse", 2, 25),
    ("Samuel", "Keyboard", 1, 50),
    ("Mary", "Laptop", 1, 800),
    ("John", "Monitor", 1, 200),
]

def order_analytics(orders):
    if not orders:  # handle empty input
        return {
            "customer_spending": {},
            "top_customer": None,
            "average_spending": 0,
            "vip_customers": []
        }
    # 1) Total money spent per customer
    customer_expenses = {}

    for customer_name, product_name, quantity, price_per_unit in orders:
        cost = quantity * price_per_unit
        customer_expenses[customer_name] = customer_expenses.get(customer_name, 0) + cost
    print(customer_expenses)

    # 2) Customer who spent the most
    top_customer = max(customer_expenses, key=customer_expenses.get)
    print(top_customer)

    # 3) Average spending across customers
    sum(customer_expenses.values())
    len(customer_name)

    total_expenses = sum(customer_expenses.values())/ len(customer_expenses)
    average_spending = round(total_expenses, 2)
    print(average_spending)


    # 4) VIP customers
    vip_customers = []

    for cusomer_name, total in customer_expenses.items():
        if total > 500:
            vip_customers.append(cusomer_name)
    print(vip_customers)

    return{
        "customer_spending" : customer_expenses,
        "top_customer": top_customer,
        "average_spending": average_spending,
        "vip_customers": vip_customers
    }

print(order_analytics(orders))

# ---------------- UNIT TESTS ----------------
class TestOrderAnalytics(unittest.TestCase):
    def test_expected_output(self):
        expected = {
            "customer_spending": {"Samuel": 850, "John": 250, "Mary": 800},
            "top_customer": "Samuel",
            "average_spending": 633.33,
            "vip_customers": ["Samuel", "Mary"]
        }
        result = order_analytics(orders)
        self.assertEqual(result, expected)

    def test_empty_orders(self):
        result = order_analytics([])
        expected = {
            "customer_spending": {},
            "top_customer": None,   # no customers
            "average_spending": 0,  # no spending
            "vip_customers": []
        }
        # Adjust function to handle empty case if needed
        self.assertEqual(result["customer_spending"], expected["customer_spending"])
        self.assertEqual(result["vip_customers"], expected["vip_customers"])

if __name__ == "__main__":
    unittest.main()