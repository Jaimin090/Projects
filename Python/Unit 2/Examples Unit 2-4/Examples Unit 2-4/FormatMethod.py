#FormatMethod.py
course = 'CPRG-216'
print('welcome to programming course {}'.format(course))

credits = 3
# most common way of including variables in formatted output
print('Course Code: {}  Credits: {:.1f}'.format(course, credits))
# allows us to change the order
print('Course Code: {1}  Credits: {0:.1f}'.format(credits, course))
