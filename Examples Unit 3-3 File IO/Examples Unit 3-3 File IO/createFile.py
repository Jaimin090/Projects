# CreateFile.py
print('create file test.txt.')
my_file= open('test.txt', 'w')
my_file.write("New line has been written to file\n")
my_file.close()   # close the file
