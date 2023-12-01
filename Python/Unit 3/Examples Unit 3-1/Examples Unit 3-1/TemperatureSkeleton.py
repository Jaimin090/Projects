# store program in a file called temperature
# new file in IDLE
def celsiusToKelvin(valueCelsius):
    '''Converts a value from degrees celsius to degree Kelvin

    Arguments:
        valueCelsius: a double
    
    Returns:
        The degrees Kelvin
    '''
    valueKelvin = 0.0
    valueKelvin = valueCelsius + 273.15
    return valueKelvin



def kelvin_to_celsius(value_kelvin):
    '''    Function: kelvin_to_celsius
    This function converts a value from degrees kelvin to degrees celsius

    Parameters: value_kelvin - required parameter (float) - a value in degrees kelvin
    Returns  : value_celsius - (float) - a value in degrees celsius'''
    pass


def main():
    """ Calls the function celsiusToKelvin for the value provided
    """
    valueC = 10.0
    print (valueC, 'C is', celsiusToKelvin(valueC), 'K')

    value_k = 283.15
    print(value_k, 'K is', kelvin_to_celsius(value_k), 'C')

if __name__ == '__main__':
    main()
