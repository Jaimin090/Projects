is_leap_year = False
input_year = int(input('Please input a year to check if it is a leap year: '))
if (input_year % 4) == 0: #  inputYear is divisible by 4    
    if (input_year % 100) == 0: #  inputYear is divisible by 100 (century year)       
        if (input_year % 400) == 0: #  inputYear is divisible by 400            
            is_leap_year = True
    else: #  inputYear is not divisible by 100        
        is_leap_year = True
if is_leap_year:
    print(input_year, 'is a leap year')
else:
    print(input_year, 'is not a leap year')


