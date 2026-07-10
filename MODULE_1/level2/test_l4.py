"""Question 3 — Group Products by Customer

This is the first new pattern after Count and Sum.

Dataset:

sales = [
    ("Samuel", "Laptop", 800),
    ("John", "Mouse", 25),
    ("Samuel", "Keyboard", 50),
    ("Mary", "Laptop", 800),
    ("John", "Monitor", 200),
    ("Mary", "Mouse", 25),
]
📋 Question

List every product purchased by each customer.

🚫 Interview Rule

Don't write code immediately.

Follow the interview framework.

Step 1

What is the input?

Step 2

What should the output look like?

Write the complete expected dictionary.

Step 3

What is the key?

Step 4

What is the transformation?

Choose one:

Count
Sum
Average
Max
Min
Sort
Group ✅

(This is our new pattern.)

Step 5

Write one dictionary entry only.

Example:

{
    "Samuel": ?
}
Step 6

Write the code.

💡 One Hint

Ask yourself these two questions:

When I see a customer for the first time, what should I create?
Every time I see that customer again, what should I do with the product?

Those two questions are enough to solve the entire problem.
"""


sales = [
    ("Samuel", "Laptop", 800),
    ("John", "Mouse", 25),
    ("Samuel", "Keyboard", 50),
    ("Mary", "Laptop", 800),
    ("John", "Monitor", 200),
    ("Mary", "Mouse", 25),
]

# List every product purchased by each customer.
product = {}

for cutomer_name, product_name, price in sales:
    if cutomer_name not in product:
        product[cutomer_name] = []
    product[cutomer_name].append(product_name)
print(product)

#  method 2 
product = {}

# for cutomer_name, product_name, price in sales:
#     product.setdefault(cutomer_name, []).append(product_name)
# print(product)