sales = [
    ("Samuel", "Laptop", 800),
    ("John", "Mouse", 25),
    ("Samuel", "Keyboard", 50),
    ("Mary", "Laptop", 800),
    ("John", "Monitor", 200),
    ("Mary", "Mouse", 25),
]

products = {}
for customer_name, product_name, price in sales:
    products[product_name] = products.get(product_name, 0) + 1
print(products)

# analytics = {}
# for customer_name, product_name, price in sales:
    
#     if customer_name not in analytics:
#         analytics[customer_name] = analytics.get(analytics, 0) + price 
#     print(analytics)   