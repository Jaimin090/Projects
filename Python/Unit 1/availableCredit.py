#availableCredit.py
creditLimit = float(input('Enter Credit Limit: '))
amountOwing = float(input('Enter amount owing: '))
availableCredit = creditLimit - amountOwing
print ('Available Credit is $', availableCredit)