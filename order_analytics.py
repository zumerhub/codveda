"""You are given a list of customer_spending orders.

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

1) Total money spent per customer_spending

Example:

{
    "Samuel": 850,
    "John": 250,
    "Mary": 800
}

Because:

Samuel = 800 + 50 = 850
John = (2×25) + 200 = 250
2) customer_spending who spent the most

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
"""

# Solution
"""
customer_spending analytics
order contains"
customer_name, product_name, quntity, price_per_unit

1. Total money spent per customer_spending
2. customer_spending who spent the most
3. Average spending across customers
4. VIP customers
"""
orders = [
    ("Samuel", "Laptop", 1, 800),
    ("John", "Mouse", 2, 25),
    ("Samuel", "Keyboard", 1, 50),
    ("Mary", "Laptop", 1, 800),
    ("John", "Monitor", 1, 200),
]
def custormer_analytics(orders):
    # 1. Total money spent per customer_spending
    customer_spending = {}

    for customer_name, product_name, quntity, price in orders:
        total_cost = quntity * price
        customer_spending[customer_name] = (
            customer_spending.get(customer_name, 0) + total_cost
        )
    print(customer_spending)
    print()

  
    #     # 2. customer_spending who spend the most
    top_customer = max(customer_spending, key=customer_spending.get)
    print(top_customer)


    #     # 3. Average Spending across customer_spending
    sum(customer_spending.values())
    len(customer_spending)

    average_spend = sum(customer_spending.values()) / len(customer_spending)
    average_spending = round(average_spend, 2)
    print(average_spending)

    #     # 4. vip customers
    vip_customers = []

    for customer_name, total in customer_spending.items():
        if total > 500:
            vip_customers.append(customer_name)
    print(vip_customers)

    return{
               "customer_spending": {
                   "customer_name": customer_name,
               },
                "top_customer": top_customer,
                "average_spending": average_spending,
                "vip_customers": vip_customers
            }
print("Output: ", custormer_analytics(orders))