def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def menu():
    print("Simple Calculator")
    print("1. Add") 
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    menu_input = int(input("Enter menu option: "))
    return menu_input

def main():
    i = 1               # Can also be solved by the ChatGPT way (while True and break)
    while i >= 0:       # Create a while loop that runs as long as i is greater than or equal to 0
        option = menu()             # the idea for defining the option is somewhat taken from ChatGPT

        if option > 0 and option < 5:                  # and used so this code block is executed only for 1 to 4 not any other number
            a = float (input("Enter first number: "))
            b = float (input("Enter second number: "))  
        if option==1:                       # add, subtract, multiply and divide functions called respectively
                    addition = add(a,b)
                    print (f"{a} + {b} = {addition}")

        elif option == 2: 
                    subtraction = subtract(a,b)
                    print (f"{a} - {b} = {subtraction}")

        elif option == 3:
                    multiplication = multiply(a,b)
                    print (f"{a} * {b} = {multiplication}")

        elif option == 4:
                    if b == 0:
                        print (f"{a} / {b} = Cannot divide by 0") # gives an error msg      
                    else:
                        division = divide(a,b)
                        print (f"{a} / {b} = {division}")
        elif option == 0:
            i = option - 1      # used to break the loop by making the value of i go less than zero
            print("Calculator app closed")
if __name__ == '__main__':
    main()