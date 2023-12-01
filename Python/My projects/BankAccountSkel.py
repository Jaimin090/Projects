# -*- coding: utf-8 -*-
"""
Created on May 3, 2023

@AUTHOR: Dave Leskiw
functions by Jaimin Chcavda 
"""

class BankAccount:
    # create the constuctor with parameters: accountNumber, name and balance 
    def __init__(self,accountNumber, customerName, balance):
       self.__account_number = accountNumber
       self.__customer_name = customerName
       self.__balance = balance
        
    # create Deposit() method
    def deposit(self , deposit ):
        self.__balance += deposit
        return self.__balance
    
    # create Withdrawal method
    def withdraw(self , withdrawAmount):
        if self.__balance >= withdrawAmount:
            self.__balance -= withdrawAmount    
            return self.__balance
        else:
            return False
        
    # create display() method
    def __str__(self):
        result = f"Account Number   :{self.__account_number} \n"
        result +=  f"Customer Name    :{self.__customer_name} \n"
        result +=  f"Balance          :{self.__balance:,.2f}"
        return result

def main():        
    # Testing the code :
    print ('Opening Balance')
    myAccount = BankAccount(487512, "Dave" , 2300)
    print (myAccount)
    # Creating Withdrawal Test
    withdraw_amount = 300.00
    print ('\nWithdrawing: ', withdraw_amount )
    ok = myAccount.withdraw(withdraw_amount)
    if ok:
        print ('Withdrawal Successful')
    else:
        print ('Withdrawal Unsuccessful')
    withdraw_amount = 3000.00

    print ('\nWithdrawing: ', withdraw_amount )
    ok = myAccount.withdraw(withdraw_amount)
    if ok:
        print ('Withdrawal Successful')
    else:
        print ('Withdrawal Unsuccessful')

    # Create deposit test
    deposit_amount = 253.29
    print ('\nDepositing', deposit_amount)
    myAccount.deposit(deposit_amount)
    # Display account informations
    print ('\nClosing Balance')
    print(myAccount)

if __name__ == '__main__':
    main()