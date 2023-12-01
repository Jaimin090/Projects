# appendToFile.py
print('open file test.txt in append mode.')
my_file = open('test.txt', 'a')
my_file.write("Add new line to file\n")
my_file.close()  # close the file
