i = 1
while i >= 0:

    print(" ")
    print("Simple Calculator")
    print("1. Add") 
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    print(" ")

    menu = int(input("Enter menu option: "))
    if menu > 0 and menu < 5:                                                                                # and used so this block of if is executed only for 1 to 4 not any other number
        number1 = float (input("Enter first number: "))
        number2 = float (input("Enter second number: "))
    i += menu                                  

    if menu == 1:
            output = number1 + number2 
            print(number1,"+",number2, "=", output )

    elif menu == 2: 
            output = number1 - number2
            print(number1,"-",number2, "=", output )

    elif menu == 3:
            output = number1 * number2
            print(number1,"*",number2, "=", output )

    elif menu == 4:
            if number2 == 0:
                print("Cannot divide by 0")       
            else:
                output = number1 / number2
                print(number1,"/",number2, "=", output )

    else:   
        i = menu - 1      # used to break the loop by making the value of i go less than zero
        print("Calculator app closed")