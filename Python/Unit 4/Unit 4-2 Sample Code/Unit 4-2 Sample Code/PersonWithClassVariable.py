#PersonWithClassVariable.py
class Person:
    __nbr_of_persons = 0               # initialize private class variable

    def __init__(self, person_name, person_age):
        self.__name = person_name
        self.__age = person_age
        Person.__nbr_of_persons += 1   # increment private class variable

    def __str__(self):
        return f"name is {self.__name}, age is {self.__age}"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, person_name):
        self.__name = person_name

    def set_age(self, person_age):
        self.__age = person_age
    
    def get_nbr_of_persons():
        return Person.__nbr_of_persons
    
per1 = Person("Amy", 23)
print(per1)
per2 = Person("Zach", 19)
print(per2)
per3 = Person("Ravi", 21)
print(per3)
print(Person.get_nbr_of_persons(), 'person objects created.')

