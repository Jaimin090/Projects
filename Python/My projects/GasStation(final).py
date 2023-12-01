print("-" * 45)
print("*** Welcome to Gas Station Supplier Program! ***")
print("-" * 45)
print("Please select the type of purchase:")
print("G: Gas")
print("O: Oil")

entry = input(">>> ").lower().strip()    #lower() makes the input lowercase, and strip() removes leading spaces

if entry == "g":                         # block for calculating before and after price of gas

    product_name = "Gas"
    litres = float(input("Enter the number of litres: "))
    before_price = litres * 1.07
    after_price = before_price

    if litres > 4000:
        after_price -= (after_price*0.10)

elif entry == "o":                       # block for calculating lires, before and after price of oil

    product_name = "Oil"
    cases_oil = int(input ("Enter # of cases of Oil: "))
    litres = cases_oil * 12
    before_price = litres * 1.27
    after_price = before_price

    if cases_oil > 8:
        after_price -= (after_price*0.10)
else:
    print("Invalid input, you should enter g/G or o/O")        # if any other value than g/G/o/O program is terminated showing invalid input
    
if (entry in 'og'):                                            # to calc provincial tax on gas and oil

    province = input("Please enter the 2 letter province abbreviation: ").lower().strip()
    x = ['ab', 'bc', 'mb', 'nt', 'nu', 'qu', 'sk', 'yt']       # here x is storing the provincial characters in form of strings

    if province in x:
        GST= after_price*0.05
    elif province == 'on':
        GST= after_price*0.13
    else:
        GST= after_price*0.15
    total_price= after_price + GST      
    # Final Output
    print("-" * 91)          
    print("Product"  f"{'# Of Litres':>20}"   f"{'Price Before':>17}"  f"{'Price After':>15}"  f"{'GST':>13}"  f"{'Total Price':>15}")   # f strings used for making the table like format
    print(product_name + f"{litres:>24.2f}" + f"{before_price:>17.2f}" + f"{after_price:>15.2f}" + f"{GST:>13.2f}" + f"{total_price:>15.2f}") # and executing the output till 2 decimal places
    print("-" * 91)
    print ("Thank you for your business, Good Bye")  