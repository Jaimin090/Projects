input_year = int(input("Enter a year (negative value to stop): "))
while input_year >= 0:
    if input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0):
        print(input_year, "is a leap year")
    else:
        print(input_year, "is not a leap year")
    input_year = int(input("Enter a year (negative value to stop): "))
print ("Complete")