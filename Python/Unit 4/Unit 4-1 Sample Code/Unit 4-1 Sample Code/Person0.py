#Person0.py
class Person:
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

person1 = Person('Maria', 36)
# request the string representation of the person1 object
# returns the address of the person1 object in memory
print(person1.__str__())
print(person1)
print(str(person1))
