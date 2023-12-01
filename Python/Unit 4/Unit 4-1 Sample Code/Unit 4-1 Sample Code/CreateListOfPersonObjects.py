#CreateListOfPersonObjects.py
# Program to create a list of Person objects
from Person import Person
def main():
    pList = []
    name = input("Enter person's name (quit to exit)")
    # Loop through and read data and create Person objects
    while name != 'quit':
        age = int (input ('Enter age: '))
        p = Person(name, age)
        # add each Person object to pList
        pList.append (p)
        name = input("Enter person's name (quit to exit)")
    # print out all name in pList
    for person in pList:
        print (person)
main()