#AppendToList.py
# append to a list
def appendToList(myList, name):
    myList.append(name)
    name = ''
nameList = ['Fred', 'John']
newName = 'Ed'
appendToList(nameList, newName)
appendToList(nameList, 'Andy')
print (nameList)