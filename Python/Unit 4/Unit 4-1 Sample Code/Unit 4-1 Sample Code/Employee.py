#solution
class Employee:

    #
    # Constructor for objects of class Employee
    #
    def __init__(self, name="", hours_worked=0, rate_of_pay=0):
        # initialise instance variables
        self.__name = name
        self.__hours_worked = float(hours_worked)
        self.__rate_of_pay = float(rate_of_pay)

    def __str__(self):
        result = (
            f"Name: { self.__name}\nHours: { self.__hours_worked} "
            f"Rate: ${ self.__rate_of_pay:.2f} "
            f"Gross Pay: ${ self.calc_gross_pay():.2f}\n"
        )
        return result

     # Accessors
     #
     # get_name(): - returns the name of the employee
     #
     # return     the employee name
     #
    def get_name(self):
        return self.__name

     #
     # get_hours(): - returns the number of hours worked
     #
     # return     the hours worked
     #
    def get_hours_worked(self):
        return self.__hours_worked

     #
     # get_rate(): - returns the rate of pay
     #
     # return     the rate of pay
     #
    def get_rate_of_pay(self):
        return self.__rate_of_pay

    # Mutators

     #
     # set_name(): - accepts a new name for the employee
     #
     # name  the new name for the employee
     #
    def set_name(self, name):
        self.__name = name

     #
     # set_hours_worked(): - accepts a new hours worked for the employee
     #
     # hours_worked  the new hours worked by the employee
     #
    def set_hours_worked(self,  hours_worked):
        self.__hours_worked = float(hours_worked)

     #
     # set_rate_of_pay(): - accepts a new rate of pay for the employee
     #
     # rate_of_pay  the new rate of pay for the employee
     #
    def set_rate_of_pay(self,  rate_of_pay):
        self.__rate_of_pay = float(rate_of_pay)

    def add_hours_worked(self,  hours_worked):
        self.__hours_worked += hours_worked

     #
     # calcGross(): Calculate are return the gross pay for
     # the employee based on the hours and rate of pay.
     #
     # return     the gross pay
     #
    def calc_gross_pay(self):
        gross_pay = self.__hours_worked * self.__rate_of_pay
        return gross_pay


