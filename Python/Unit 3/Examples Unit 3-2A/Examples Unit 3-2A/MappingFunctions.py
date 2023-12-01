#MappingFunctions.py
def doubleit(x):
    return x + x
def main():
    ATuple = (1, 2, 3.7, 'ABC') 
    numSqList = list(map(doubleit, ATuple))
    print (numSqList)
if __name__ == "__main__":
    main()

