print("---------------------------------------------")
print("*** Welcome to Gas Station Supplier Program! ***")
print("---------------------------------------------")
print("Please select the type of purchase:")
print("G: Gas"
      "\nO: Oil")

purchase =  str(input(">>> "))    # 1st part is still incomplte, gasprice code is starts

litres_gas = int(input("Enter the number of litres of gas: ")) 

gas_price = litres_gas * 1.07

print("Please enter the 2 letters province abbreviation: ")

if litres_gas > 4000:
    gas_price = gas_price - (gas_price  * 0.1) # we would have to use the f string i.e 2f  

    print("# of litres of gas", litres_gas,
          "\nCost of gas is",gas_price, "$")
else:
    print("# of litres of gas", litres_gas,
          "\nCost of gas is",gas_price, "$")
    
cases_oil = int(input ("Enter the number of cases of oil: ")) # GST calculation left for gas, oilprice code starts

litres_oil = cases_oil * 12
oil_price = litres_oil * 1.27

print("Please enter the 2 letters province abbreviation: ")

if cases_oil > 8:
    oil_price = oil_price - (oil_price * 0.1)

    print("# of litres of oil", litres_oil,
          "\nCost of oil is",oil_price, "$")
else:
    print("# of litres of oil", litres_oil,
          "\nCost of oil is",oil_price, "$")
    
print("---------------------------------------------------------------------------------------------")
print("Product \nOil")
print("---------------------------------------------------------------------------------------------")

print("Thanks for your business, Good Bye")