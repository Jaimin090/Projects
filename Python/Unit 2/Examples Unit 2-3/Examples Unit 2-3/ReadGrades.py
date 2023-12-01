num = int(input("How many grades do you want to enter? "))
counter = 0   #     how many times u want loop to run
total = 0   # add the grades
while counter < num:
    grade = float(input("Enter grade: "))
    total += grade
    counter += 1
print("The average grade is ", total / num)

