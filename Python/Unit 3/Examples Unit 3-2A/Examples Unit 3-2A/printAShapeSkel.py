#printAShapeSkel.py
# Global Constants, pixel is the character to use for output
pixel = '*'
def main():
    ''' main - function to control print a shape. Display menu, enters
    user select and calls the appropriate functions
    Arguments: None
    Returns: None '''
    # input menu selection
    select = menu()
    # while selection is not 0
    while select != 0:
        # if select is 1 call line()
        if select == 1:
            line()
        # else if select is 2 call box()
        elif select == 2:
            box()
        # else if select is 3 call square()
        elif select == 3:
            square()
        # else print invalid selection
        else:
            print ("Invalid selection")
        # input menu selection
        select = menu()

def menu():
    ''' Menu - function to print menu of options and input a select
    from the user
    Arguments: None
    Returns: the selection from the user
    ''' 
    print ('Print a shape')
    print()
    print ('1. Line')
    print ('2. Box')
    print ('3. Square')
    print ('0. Exit')
    selection = int(input('Enter selection: '))
    return selection
def line():
    ''' line - function to draw a line using the global variable 'pixel'. Prompts
    user for the length of the line.
    Arguments: None
    Returns: None
    '''
    length = int(input ("Input length for the line: "))
    print_line (length)
def print_line(number):
    ''' print_line(number) - prints a line of 'pixel' characters 'number' characters long
    Arguments: number - length of the line
    Returns: None'''
    print (pixel * number)
def box ():
    ''' box - input the width and height from the user a draws a box of that size
    Arguments: None
    Returns: None'''
    w = int (input ('Enter the width: '))
    h = int(input ("Enter the height: "))
    print_box (w, h)    
def print_box(width, height):
    '''print_box(width, height) - draw a box of 'pixel' characters of size
    width x height. Use print_line() to draw the top and the bottom line of the box.
    Arguments:
        height - height of the box
        length - length of the box'''
    # print top of the box
    print_line (width)
    # print the sides
    for i in range (height-2):
        print (pixel, end = '')
        # number of spaces is width - 2
        print (' '*(width-2), end = '')
        # print pixel and advance a line
        print (pixel)
    # print bottom of the box
    print_line (width)

def square():
    '''Square - input the size of from the user a draws a square using the
    function print_box
    Arguments: None
    Returns: None'''
    size = int (input ("Enter the size: "))
    print_box (size, size)
 
if __name__ == "__main__":
    main()


