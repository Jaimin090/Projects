# Pay and Go Evening Parking
# The parking software system being developed is different from
# other traditional parking systems in that drivers don’t need to put a ticket 
# on their dash, all they need to do is provide their license plate number in conjunction
# with a credit card  number. There are two types of users who can use the program. 
# The driver user who can register the vehicle when entering the parking lot. The administrator
# user who can verify that a vehicle is in the lot, removing a vehicle from the lot, clear the lot,
# display all vehicles and charges. The administrator should enter a valid password (assume it is password)
# to access the administration functionalities. 
# Program uses two parallel lists to track license Plates and credit card numbers
# Date: Nov 1, 2023
# Original Author: Dave Leskiw
# Assistant Authors: Aman Sharma, Jaimin Chavda, Michael(Zi) Liang
# global variable
from datetime import date
SPOTS = 5
PASSWORD = 'apple'
def password_valid ():
    '''
    password_checker - inputs and validates a password for administrator related functions
    Password is stored in a global variable called 'PASSWORD'. 
    Arguments:
        none
    Return Value:
        true - if the input password matches the password stored in the variable 'PASSWORD' otherwise false
    '''
    print("Administrative Function")
    selection = input("Enter the password: ")
    while True:
        if selection == PASSWORD:
            return True
        else:
            return False

def printMenu():
    ''' printMenu - will display the customer menu, input a validate selection and return that select
    Arguments: none
    Return Value: the selection as an integer
    '''
    options = {0: 'Test populate -- FOR TESTING ONLY', 1:'Register a vehicle', 2:'Verify vehicle registration', 3:'Display registered vechicles and save to file (Admin only)',
               4: 'Display daily charges and save to file (Admin only)',  5: 'Clear Vehicles (Admin only)', 6: 'Exit'}
    for s, option in options.items():
        print (str(s)+':' + option)
    select = int(input ('Enter your selection: '))
    while select not in options:
        select = int(input ('Enter your selection: '))
    return select
def register_vehicle(plates, cc_numbers):
    ''' register_vehicle - if there is room in the parking lot, input the license plate and cc number and
        add the vehicle to the lot
        Arguments: 
            license - a list of license plates numbers 
            cc_numbers - a list of related cc numbers to be charged
        Returns:
            None
    '''
    if len(plates) <= SPOTS:
        print("The Parking lot has room for you")
        input_plate_number = input("Enter your plate number: ")
        input_cc_number = int(input("Enter your Credit Card Number ($4.00 charge): "))
        plates.append(input_plate_number)
        cc_numbers.append(input_cc_number)
    else:
        print ("Parking Lot Full! Please wait until some spots are available.")


def verify_vehicle(plate, plates):
    '''verify_vehicle - verifies that 'plate' is in the parking lot. Return true
    if the plate is in the lot, false otherwise.
    Arguments:
        plate - plate to be check
        plates - list of all plates currently in the lot
    Return value:
        boolean - returns true if the plate is found in the lot otherwise false
    '''
    if plate in plates:         # Checking if an element exists in the list
        return True
    else:
        return False

def display_registered_vehicles (plates):
    '''display_registered_vehicles - will print a report (to the screen and
       a file) of all vehicles registered in the lot. It will output to a local
       file called 'PlateReport.txt'. This is a administration only function that is
       password protected.
       Arguments:
        plates - a list of all the plates (vehicles) current registered
       Return Value:
        none
    '''
    print("Today's date: ", date.today())
    print('')
    print("Registered Plates")
    print("=" * 20)
    for plate in plates:
        print(f"{plate:>8}")

    file = open('PlateReport.txt', 'a')
    file.write(f"Today's date: {date.today()}\n")
    file.write('\n')
    file.write("Registered Plates\n")
    file.write(f"{'=' * 20}\n")
    for plate in plates:
        file.write(f"{plate:>8}\n")
    file.close()

def display_daily_charges (plates, cc_numbers):
    '''
    display_daily_charges - produces a report of all charges for the parking lot based on the plates and cc_numbers list.
    Output is directed to the screen and an output file.
    Arguments:
        plates - is a list of all the vehicle plate numbers
        cc_numbers - is a list of credit card number associated with each plate
    Return Value:
        None
    '''
    CHARGE = 4
    total = 0
    print("Daily Parking Summary for ", date.today())
    print("")
    print(f"{'Plate':>10} {'CC Number':>30} {'Charge':>10}")
    print("=" * 52)
    for i in range(len(plates)):
            print(f"{plates[i]:>10} {cc_numbers[i]:>30} {CHARGE:>10.2f}")
            total += CHARGE
    print("=" * 52)
    print(f"{total:>52.2f}")

    file2 = open('DailyCharges.txt', 'a')
    total = 0
    file2.write(f"\nDaily Parking Summary for {date.today()}\n")
    file2.write("\n")
    file2.write(f"{'Plate':>10} {'CC Number':>30} {'Charge':>10}\n")
    file2.write(f"{'=' * 52}\n")
    for i in range(len(plates)):
        file2.write(f"{plates[i]:>10} {cc_numbers[i]:>30} {CHARGE:>10.2f}\n")
        total += CHARGE
    file2.write(f"{'=' * 52}\n")
    file2.write(f"{total:>52.2f}")
    file2.close()
    
def clear_vehicles (plates, cc_numbers):
    '''
    clear_vehicles - clears out ALL cars for the lot, resetting the plates and cc_numbers lists
    to empty. This is an adminstrator protected function.
    Arguments:
        plates - is a list of all the vehicle plate numbers
        cc_numbers - is a list of credit card number associated with each plate
    Return Value:
        None    
    '''
    plates.clear()
    cc_numbers.clear()
       
def main():
    # create a empty list to store the  plates
    plates = []
    # create an empty list to store the credit card numbers
    cc_numbers = []
    s = printMenu()
    while (s != 6):
        match s:
            # Test populator
            case 0: 
                # test set of plates that can be used to verify functions 2,3,4, 5
                plates = ['AAA111', 'BBB222', 'CCC333', 'DDD444']
                cc_numbers = ['4100-2033-2334-9405', '5100-2309-4353-1283', '4000-1203-4842-5843', '5100-3300-1293-2394']
            # Register Vehicle
            case 1: 
                register_vehicle (plates, cc_numbers)
            # Verify Registration
            case 2:
                plate = input ("Enter the plate number to be searched: ")
                if (verify_vehicle (plate, plates)):
                    print ("Plate is registered")
                else:
                    print ("Plate is not registered")
            # Display registered vehicles and save to file (Admin only function)
            case 3:
                # check password
                if (password_valid()):
                    display_registered_vehicles (plates)
                else: 
                    print ("Invalid password")
            # Display daily charges (Admin only function)
            case 4:
                if (password_valid()):
                    display_daily_charges (plates, cc_numbers)
                else:
                    print ("Invalid password")
            # Clear vehicles (Admin only function)
            case 5:
                if (password_valid()):
                    clear_vehicles (plates, cc_numbers)
                else: 
                    print ("Invalid password")
        print(" ")
        s = printMenu()

if __name__ == '__main__':
    main()