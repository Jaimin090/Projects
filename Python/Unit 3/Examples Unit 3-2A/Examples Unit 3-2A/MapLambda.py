#MapLambda.py
def main():
    ATuple = (1, 2, 3.7, 'ABC') 
    numSqList = list(map(lambda n: n+n, ATuple))
    print (numSqList)
if __name__ == "__main__":
    main()

