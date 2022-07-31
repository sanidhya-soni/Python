import random

students = ['Sanidhya', 'Prakhar', 'Mansi', 'Sharma', 'Alex']
stud_score = {
    names: random.randint(1, 100) for names in students
}

# print(stud_score)

passed_stud = {key: score for (key, score) in stud_score.items() if score > 50}

print(stud_score)
print(passed_stud)
