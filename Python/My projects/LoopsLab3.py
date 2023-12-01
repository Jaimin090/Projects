sum = 0
i = 0
number1 = int(input("Enter the number > 1: "))
while i < number1:                                                   # loop ends when i < number1 becomes unsatisfied
    i += 1                                                           # i = i + 1
    sum += i                                                         # sum = sum + i
    average = sum/number1
print(" ")                                                           # indentation very imp for lines 8 and 9
print("The average of the integers 1...",number1 ,"is", average)     # we can take avg at the end also just by writing sum/number1 instead of average