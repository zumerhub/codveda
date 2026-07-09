# sorting are the process of data into a specific order. usually ascending or desending
scores = {
    "John": 75,
    "Mary": 98,
    "Samuel": 90,
    "Alice": 85,
   
}

print(scores.items())

"""
dict_items is a special python object that provides a view of the key-value pairs in a dict. 
"""
sorted_scores = sorted(scores.items(), key=lambda item: item[1])
print(f"lowest", sorted_scores)

sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print(f"highest", sorted_scores)

# print(scores.items[0])

