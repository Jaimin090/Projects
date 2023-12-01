#ArgVarLenDict.py
# A dictionary is passed in
def printPrices(**k):
    for productName, price in k.items():
        print(f"The price of {productName} is {price:.2f}")

printPrices(ABC=11.95, widget=23.50, piano=4400.0)

