grade = float (input ("Enter grade: "))
if grade >= 90:
    lGrade = 'A'
elif grade >= 75:
    lGrade = 'B'
elif grade >= 60:
    lGrade = 'C'
elif grade >= 50:
    lGrade = 'D'
else:
    lGrade = 'F'
print (lGrade)