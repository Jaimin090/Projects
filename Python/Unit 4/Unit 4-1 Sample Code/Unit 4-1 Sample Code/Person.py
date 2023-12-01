#Person.py
class Person:
    def __init__(self, person_name, person_age):
        self._name = person_name
        self._age = person_age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    
    def set_name(self, person_name):
        self._name = person_name

    def set_age(self, person_age):
        self._age = person_age

    def __str__ (self):
          return f"Name is {self._name}, age is {self._age}"
 