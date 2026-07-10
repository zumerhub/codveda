scores = [80, 65, 95, 70, 88]

print(f"initial---", scores)
"""
This is a List use sort
"""

print("ascending----", sorted(scores))
sorted_scores = sorted(scores, reverse=True)
print(f"descending----", sorted_scores)
print()


# Question 2
names = ["Mary", "John", "Samuel", "Ade"]

print(f"initial -- ", names)

# Sort the names
sorted_names = sorted(names)
print(f"ascending sorted names: ", sorted_names )

# decending sorted
descending_sorted = sorted(names, reverse=True)
print(f"descending_sorted :", descending_sorted)

