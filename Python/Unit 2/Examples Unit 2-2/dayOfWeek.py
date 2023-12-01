dayOfWeek = int (input ("Enter the day (Monday = 1): "))
time = int (input ("Enter time: "))
barFlag = dayOfWeek == 5 and time > 1700
# you can write or also instead of and
if barFlag:
    print ("Go have a drink")
else:
    print ("Time to study")

