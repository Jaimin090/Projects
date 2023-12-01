#Time1.py
class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0

my_time = Time()
# Initial value
print ('Initial values')
print('{} hours'.format(my_time.hours), end=' ')
print('and {} minutes'.format(my_time.minutes))
my_time.hours = 7
my_time.minutes = 15
print ('After assignments')
print('{} hours'.format(my_time.hours), end=' ')
print('and {} minutes'.format(my_time.minutes))
torontoTime = Time()
torontoTime.hours = 9
torontoTime.minutes = 15
print (f"Time in Toronto is {torontoTime.hours:2d}:{torontoTime.minutes:02d}")

