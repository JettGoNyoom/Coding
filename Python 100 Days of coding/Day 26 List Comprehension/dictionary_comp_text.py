# Dictionary comprehension
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# student_scores = {new_key:new_value for item in list}
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

# students that passed thru dictionary comprehension
# passed_students = {new_key:new_value for (key, value) in dictionary.items() if test}
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)