#ListForLoop.py
# if you use a for loop you can not alter the contents of the list
gradeList = [76.3, 97, 88.2, 67.5, 100]

sumGrades = 0
for grade in gradeList:
    sumGrades += grade

average = sumGrades / len(gradeList)
print ('The average grade for the class is', format(average,'.2f'))
