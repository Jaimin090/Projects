#Time2.py
class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0
    
    def print_time(self):
        print('{} hours'.format(self.hours), end=' ')
        print('and {} minutes'.format(self.minutes))

my_time = Time()
my_time.hours = 7
my_time.minutes = 15
my_time.print_time()

