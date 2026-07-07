"""Let's make it a little more realistic.
students = {
   "Samuel": [85, 90, 78],
   "Mary": [95, 88],
   "John": [70, 82, 79],
   "Alice": [99, 96, 100],
   "David": [60, 65, 58]
}
Your task
Create a dictionary called:
average_scores = {}
After your loop, it should become:
{
   "Samuel": 84.33,
   "Mary": 91.5,
   "John": 77.0,
   "Alice": 98.33,
   "David": 61.0
}
Rules
Use one loop.
Use .items().
Use sum().
Use len().
Use round().
Do not print inside the loop.
Store the result in the dictionary.
This is exactly how analytics systems prepare data before creating reports or dashboards.
"""

# Solution
students = {
   "Samuel": [85, 90, 78],
   "Mary": [95, 88],
   "John": [70, 82, 79],
   "Alice": [99, 96, 100],
   "David": [60, 65, 58]
}

# print(students.items())
average_scores = {}
for student_name, scores in students.items():
    avg_score = round(sum(scores) / len(scores), 2)
    average_scores[student_name] = avg_score
print(average_scores )