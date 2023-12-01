def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def menu():
    # Displays menu options
    print("Simple Calculator")
    print("1. Add") 
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    menu_input = input("Enter menu option: ")
    
    # Validate user input so if its a string or any other number input is asked again
    while True:
        if menu_input in ("1", "2", "3", "4", "0"):
            return menu_input     # this allows to exit the loop and take the valid input to the next block of code
        else:                     # ChatGPT in a different program showed that its not compulsory to put return at the end of function(so some of that logic used)
            menu_input = input("Enter menu option: ")

def main():
    i = 1                                   # Can also be solved by the ChatGPT way (while True and break)
    while i >= 0:                           # loop that runs as long as i is greater than or equal to 0 thus exits if value is negative(less than zero)
        option = menu()                     # the idea for defining the option is somewhat taken from ChatGPT
        selection = int(option)             # $$$ most imp line $$$ i wasnt able to figue this out (converts to integer)
                # another way too to put in menu()
                # while menu_input not in ("1", "2", "3", "4", "0"):
                # menu_input = (input("Enter menu selection: "))           
            
        if selection > 0 and selection < 5:                 # and used so this code block is executed only for 1 to 4 not any other number
            a = float (input("Enter first number: "))
            b = float (input("Enter second number: "))  
            if selection==1:                                # add, subtract, multiply and divide functions called respectively
                    addition = add(a,b)
                    print (f"{a} + {b} = {addition}")

            elif selection == 2: 
                    subtraction = subtract(a,b)
                    print (f"{a} - {b} = {subtraction}")

            elif selection == 3:
                    multiplication = multiply(a,b)
                    print (f"{a} * {b} = {multiplication}")

            elif selection == 4:
                    if b == 0:
                        print (f"{a} / {b} = Cannot divide by 0") # gives an error msg      
                    else:
                        division = divide(a,b)
                        print (f"{a} / {b} = {division}")
        elif selection == 0:
            i = selection - 1                                     # used to break the loop by making the value of i go less than zero
            print("Calculator app closed")
if __name__ == '__main__':
    main()