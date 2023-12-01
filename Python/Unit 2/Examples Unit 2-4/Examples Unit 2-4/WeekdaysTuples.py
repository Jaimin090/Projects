week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
# write  a loop to print out all the days of the week
print("Week: ")
for day in week:
    print (day, end = ' ')
print()

print("Weekdays: ")
weekdays = week[1:6]
# write  a loop to print out the week days
for day in weekdays:
    print (day, end = ' ')
print()

print("Weekend: ")
weekend = week[6:]+week[:1]
# write  a loop to print out the weekend days
for day in weekend:
    print (day, end = ' ')
print()

# input a day of the week
day = input ("Enter the day of the week: ")
# if the day of the week IN weekdays
if day in weekdays:
    # print this is a weekday
    print ("This is a normal week day")
elif day in weekend:
    print("This is a weekend")
else:
    print("Invalid Input")