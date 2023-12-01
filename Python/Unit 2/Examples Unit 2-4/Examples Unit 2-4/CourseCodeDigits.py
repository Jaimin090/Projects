
course = input ('Enter Course Code: ')
pos = 0
digits = 0
while pos < len(course):
    if course[pos].isdigit():
        digits += 1
    pos += 1

print('There are', digits, 'digits in', course)
