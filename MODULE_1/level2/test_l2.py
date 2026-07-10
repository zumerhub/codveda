sales = [
    ("Samuel", "Laptop", 800),
    ("John", "Mouse", 25),
    ("Samuel", "Keyboard", 50),
    ("Mary", "Laptop", 800),
    ("John", "Monitor", 200),
    ("Mary", "Mouse", 25),
]
"""
# 1. What is the input?
customer_name, product_name, price

# 2. What is the expected output?
What should the output look like?
The question is:
Calculate the total amount spent by each customer.

# 3. What transformation is needed?

# 4. Then write the code.
"""

total_amount = {}
for customer_name, product_name, price in sales:
    total_amount[customer_name] = total_amount.get(customer_name, 0) + price
print(total_amount)


# Question 2
product = {}
for customer_name, product_name, price in sales:
    product[product_name] = product.get(product_name, 0) + 1 
print(product)

customer_product = {}
for custome_name, product_name, price in sales:
    customer_product[customer_name] = customer_product.get(custome_name, 0) + 1
print(customer_product)