"""Input:
sales = [
   ("Samuel", "Laptop", 800),
   ("John", "Mouse", 25),
   ("Samuel", "Keyboard", 50),
   ("John", "Monitor", 200),
   ("Mary", "Laptop", 800)
]
Each tuple:
(customer_name, product_name, amount)
Example:
("Samuel", "Laptop", 800)
means:
customer = Samuel
product = Laptop
amount = 800

Tasks
1. Total spending per customer
Expected:
{
   "Samuel": 850,
   "John": 225,
   "Mary": 800
}

2. Product purchase count
Expected:
{
   "Laptop": 2,
   "Mouse": 1,
   "Keyboard": 1,
   "Monitor": 1
}

3. Nested analytics per customer
Expected:
{
   "Samuel": {
       "orders": 2,
       "total_spent": 850
   },
   "John": {
       "orders": 2,
       "total_spent": 225
   }
}


"""

# Solution
"""1. Total spending per customer

Expected:

{
    "Samuel": 850,
    "John": 225,
    "Mary": 800
}
"""
sales = [
    ("Samuel", "Laptop", 800),
    ("John", "Mouse", 25),
    ("Samuel", "Keyboard", 50),
    ("John", "Monitor", 200),
    ("Mary", "Laptop", 800)
]

# (customer_name, product_name, amount)

totat_spending = {}

for customer_name, product_name, amount in sales:
    totat_spending[customer_name] = totat_spending.get(customer_name, 0) + amount
# print(totat_spending)

"""2. Product purchase count
Expected:
{
   "Laptop": 2,
   "Mouse": 1,
   "Keyboard": 1,
   "Monitor": 1
}
"""
print('----'*30)
products = {}
for customer_name, product_name, amount in sales:
    products[product_name] = products.get(product_name, 0) + 1
print(products)
print('----'*30)
"""
3. Nested analytics per customer
Expected:
{
   "Samuel": {
       "orders": 2,
       "total_spent": 850
   },
   "John": {
       "orders": 2,
       "total_spent": 225
   }
}
"""
analytics = {}

for customer_name, product_name, amount in sales:

    if customer_name not in analytics:
        # initialize customer here
        analytics[customer_name] = {"orders":0, "total_spent": 0}
        
    analytics[customer_name]["orders"] += 1
    analytics[customer_name]["total_spent"] += amount
            
print(analytics)



