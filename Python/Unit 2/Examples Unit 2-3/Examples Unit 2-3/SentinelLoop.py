counter = 0
total = 0
grade = float(input("Enter grade (or negative value to end): "))
while grade >= 0:
    total += grade
    counter += 1
    grade = float(input("Enter grade (or negative value to end): "))
print("The average grade is", total / counter)

