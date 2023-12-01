# readWholeFile.py
print('Opening file myfile.txt.')
my_file= open('myfile.txt', 'r')
data = my_file.read()
print (data)
my_file.close()
