#UsingMain.py
# notice that main is the first method to execute
def process1():
    print("Running process 1")

def process2():
    print("Running process 2")

def main():
    print("Starting up the program")
    process1()
    process2()
    print("Shutting down the program")

if __name__ == "__main__":
    main()
 
