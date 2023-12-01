#ListWhileLoop.py
nameList = ['Ed', 'Joe', 'Fred', 'Jane', 'Joe']
pos = 0

while pos < len(nameList):
    nameList[pos] = nameList[pos].upper()
    pos += 1

print(nameList)
