# lottry_players = [
# {
#     'name': 'Rolf',
#     'numbers': (1, 23, 56, 7, 34)
# },
# {
#     'name': 'John',
#     'numbers': (4, 23, 56, 7, 34)
# }
# ]
#
# universities = [
#     {
#         'name': 'Oxford',
#         'location': 'UK'
#     },
#     {
#         'name': 'MIT',
#         'location': 'US'
#     }
# ]
#
# lottry_players[0].total()

student = {
    'name':'Jose',
    'school':'Computing',
    'grades': (66, 77, 88)
}

def average_grade(data):
    grades = student['grades']
    return sum(grades)/len(grades)

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in stundent_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    return total / count
