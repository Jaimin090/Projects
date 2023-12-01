
course = input ('Enter a course code: ')
alpha = 0
for ch in course:
    if ch.isalpha():
        alpha += 1
print('There are' , alpha, 'alphabetic characters in', course)
