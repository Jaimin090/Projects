def menu():
    print('''Simple Calculator
1. Add
2. Subtract
3. Multiply
4. Divide
0. Exit''')

def add(a,b):
    sum=a+b
    result=sum
    return result
    
def sub(a,b):
    Difference=a-b
    result=Difference
    return result

def multiply(a,b):
    Multipilication=a*b
    return Multipilication

def divide(a,b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        Result=a/b
        return Result

def main():
    menu()
    option=input("enter menu option:")
    while option != "0":
        if "1"<=option<="4":
            FirstNumber=float(input("Enter first number:"))
            SecondNumber=float(input("Enter second number:"))
            if option == "1":
                print(f'{FirstNumber} + {SecondNumber} = {add(FirstNumber,SecondNumber)}')
            elif option == "2":
                print(f'{FirstNumber} - {SecondNumber} = {sub(FirstNumber,SecondNumber)}')
            elif option == "3":
                print(f'{FirstNumber} * {SecondNumber} = {multiply(FirstNumber,SecondNumber)}')
            elif option == "4": 
                if SecondNumber == 0:
                    print(f'{FirstNumber} / {SecondNumber}= Cannot divide by 0')
                else:
                    print(f'{FirstNumber} / {SecondNumber} = {divide(FirstNumber,SecondNumber)}')
            menu()
        option=input("enter menu option:")
    print("Calculator Closed")

if __name__=="__main__":
    main()
    
