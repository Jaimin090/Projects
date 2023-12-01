#ArgsKeyword.py
def printPrice(productName, price):
    print(f"The price of {productName} is {price:.2f}")

printPrice(productName="ABC", price=11.95)
printPrice(price=11.95, productName="ABC")


