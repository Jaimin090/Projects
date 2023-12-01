#Time3.py
class Time:
    """ A class that represents a time of day """
    def __init__(self, hours, mins):
        self.hours = hours
        self.minutes = mins
    
hours = input("Enter hours: ")
mins = input("Enter minutes: ")
my_time = Time(hours, mins)
print('{} hours'.format(my_time.hours), end=' ')
print('and {} minutes'.format(my_time.minutes))


