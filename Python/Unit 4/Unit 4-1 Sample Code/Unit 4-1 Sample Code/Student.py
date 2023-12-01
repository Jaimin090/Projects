#Student.py
class Student:

    def __init__(self, fname, lname, grade):
        self._first_name = fname
        self._last_name = lname
        self._grade = grade

    def __str__(self):
        result = f"{self._first_name:>10s}{self._last_name:>10s}{self._grade:10.2f}"
        return result
    def getGrade(self):
        return self._grade
