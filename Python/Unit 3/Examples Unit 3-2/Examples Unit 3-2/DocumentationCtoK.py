#DocumentationCtoK.py
# store program in a file called temperature
from temperature import *

def main():
    """ Calls the function celsiusToKelvin for the value provided
    """
    valueC = 10.0
    print (valueC, 'C is', celsiusToKelvin(valueC), 'K')
    # Two ways to show the doc string
    print(celsiusToKelvin.__doc__)
    help(celsiusToKelvin)


if __name__ == '__main__':
    main()
