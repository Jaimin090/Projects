# WhileLoopReadMyfile.py
print('Opening file myfile.txt.')
my_file= open('myfile.txt', 'r')
# print each line of file
line = my_file.readline()
while line != '':
    line = line.rstrip() # strip off linespace (e.g. \n)
    print(line)
    line = my_file.readline()
my_file.close()

