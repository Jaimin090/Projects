#GetGrades.py
# sample getGrades program
def getGrade():
    validGrades = ('A', 'B', 'C', 'D', 'F')
    grade = ''
    while grade not in validGrades:
        grade = input('Enter grade: ').upper()
    return grade

newGrade = getGrade()
print(newGrade)
