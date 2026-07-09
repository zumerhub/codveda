students = {
    "Samuel": [85, 90, 78],
    "Mary": [95, 88],
    "John": [70, 82, 79]
}

"""
1. Task 
students = {
   "Samuel": [85, 90, 78],
   "Mary": [95, 88],
   "John": [70, 82, 79]
}
With this structure, you'll learn to answer questions like:
What is Samuel's average score?
Who has the highest average?
How many exams did each student take?

"""
print('first iteration')
print(students['Samuel'])
print(students['Mary'][0])
print(students["John"][2])



"""
2. Task
Print:

Samuel's highest score.
Mary's number of scores.
John's total score.

💡 Hint: Think about Python functions you may already know:

max(...)
len(...)
sum(...)

You don't need a for loop yet.
"""
print('second iteration')
print(max(students['Samuel']))
print(len(students["Mary"]))
print(sum(students['John']))



"""
3. Task
Print:

Samuel's average score.
Mary's average score.
John's average score.

Use only:
sum()
len()
division (/)
round(..., 2)

Don't use a loop yet.

"""
print('third iteration')
(sum(students["Samuel"])) 
(len(students["Samuel"]))
samuel_score = (sum(students["Samuel"])) / (len(students["Samuel"]))
samuel_avg_score = round(samuel_score, 2)
print(f"samuel_avg_score ", samuel_avg_score)



sum(students["Mary"])
len(students["Mary"])
mary_score = sum(students["Mary"]) / len(students["Mary"])
mary_avg_score = round(mary_score, 2)
print(f"mary_avg_score ", mary_avg_score)


sum(students["John"])
len(students["John"])
john_score = sum(students["John"]) / len(students["John"])
john_avg_score = round(john_score, 2)
print(f"john_avg_score", john_avg_score)

print('-'*30)



students = {
    "Samuel": [85, 90, 78],
    "Mary": [95, 88],
    "John": [70, 82, 79]
} 
"""
loop throug using "for student_name, scores in students.items():" 
"""
for student_name, scores in students.items():
    avg_score = round(sum(scores) / len(scores), 2)
    
    print(student_name, avg_score)