#ReadMyfile.py
print('Opening file myfile.txt.')
my_file= open('myfile.txt', 'r')
# print each line of file
for each_line in my_file:
    each_line = each_line.rstrip()
    print(each_line)
my_file.close()