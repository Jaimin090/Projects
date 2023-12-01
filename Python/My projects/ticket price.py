age = float (input('Enter the age' ))
if age < 6:
   ticketprice = 0
else:
   if age < 12: 
       ticketprice = 5
   else:
       ticketprice = 10
print ("The ticketprice",ticketprice)