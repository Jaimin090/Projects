#Person1.py
class Person:
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age
    def __str__(self):
        return f"name is {self.name}, age is {self.age}"

person1 = Person('Maria', 36)
# reference person1 as a string
print(person1)

