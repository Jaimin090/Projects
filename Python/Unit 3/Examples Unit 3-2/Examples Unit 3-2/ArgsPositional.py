#ArgsPositional.py
def printPrice(productName, price):
    print(f"The price of {productName} is {price:.2f}")

printPrice("ABC", 11.95)
printPrice(11.95, "ABC") # results in an error as "ABC" can not be output as .2f

