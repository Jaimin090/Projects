# CPRG 216-J Assignment 2 - Programming Strategies
# Jaimin Chavda, Michael (Zi) Liang, Aman Sharma (Oregano), SAIT, 
# Oct 25, 2023

def minimum_percentage(purchase_price):
    """
    Function to calculate minimum down payment, in percent, given purchase price.
    """
    if purchase_price <= 500000:
        return 5           # 5% for <= 500,000
    elif purchase_price > 1000000:
        return 20              # 20% for > 1,000,000
    else:
        min_downpay = 500000 * 0.05 + (purchase_price - 500000) * 0.1
        min_percentage = (min_downpay/purchase_price) * 100
        return min_percentage                         

    # $$$ Alternate Way $$$ keep this

    # while not (5 <= percentage_downpay < 100):   
    #     print("Please enter a value between the minimum and 100")
    #     percentage_downpay = int(input("Enter down payment percentage: "))
        
    # if purchase_price <= 500000 :               
    #     min_downpay = purchase_price * 0.05    
                
    # elif purchase_price <=1000000:
    #     min_downpay = 500000 * 0.05 + (purchase_price - 500000) * 0.1
    #     min_percentage = (min_downpay/purchase_price) * 100     
    #     print(min_percentage)

    # else:
    #     while not (20<= percentage_downpay <100):      
    #         print("Please enter a value between the minimum and 100")
    #         percentage_downpay = int(input("Enter down payment percentage: "))
    #     min_downpay = purchase_price * 0.2
    
def main():
    name = input("Enter client name: ")
    address = input("Enter address of property: ")
    purchase_price = int(input("Enter purchase price: "))                        
    percentage_downpay = float(input(f"Enter down payment percentage (minimum {minimum_percentage(purchase_price):.3f}): "))

    while (not minimum_percentage(purchase_price) <= percentage_downpay < 100):      # This while loop continues to run until a valid percentage is entered
        print("Please enter a value between the minimum and 100")
        percentage_downpay = float(input(f"Enter down payment percentage (minimum {minimum_percentage(purchase_price):.3f}): "))
        # (i.e, between minimum percentage required for the purchase price and 100%)
        # else:                                                                          
        # print(f"Down payment percentage: {percentage_downpay:.0f}%")

    if percentage_downpay < 10:     # if block for getting the mortgage insurance premium rate according to the percentage for downpayment
        mortgage_premium = 4
    elif percentage_downpay < 15:
        mortgage_premium = 3.1
    elif percentage_downpay < 20:
        mortgage_premium = 2.8
    else:
        mortgage_premium = 0

    downpayment = purchase_price * (percentage_downpay/100)    # Downpayment based on the percentage 
    print(f"Down payment amount is ${downpayment:.0f}")

    insurance_cost = (purchase_price - downpayment) * mortgage_premium/100     # insurance calculated using the Mortgage Insurance Premium rate
    print(f"Mortgage insurance price is ${insurance_cost:.0f}")

    principal_amount = purchase_price - downpayment + insurance_cost    # The final principal amount
    print(f"Total mortgage amount is ${principal_amount:.0f}")


    mortgage_rates = {1:5.95, 2:5.9, 3:5.6, 5:5.29, 10:6}       # using dictionaries for getting the intrest rate based on the term
    term = int (input ('Enter mortgage term (1, 2, 3, 5, 10): '))
    while term not in mortgage_rates :
        print ('Please enter a valid choice')
        term = int (input ('Enter mortgage term (1, 2, 3, 5, 10): '))
    intrest_rate = mortgage_rates[term]          


    valid_amortization = [5, 10, 15, 20, 25]                    # amortization period asked from user using while loop,code is similar to the block above
    amortization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
    while amortization not in valid_amortization :
        print ('Please enter a valid choice')
        amortization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
        
    print (f"Intrest rate for the term will be {intrest_rate:.2f}%")           

    power = 1/12                            # for some reason 1/12 directly put in Emr desnt work
    Emr = (((1 + intrest_rate/200) ** 2) ** power) - 1      # Emr is the Effective Monthly Rate
    amortization_months = amortization * 12
    monthly_payment = principal_amount * ((Emr * ((1 + Emr) ** amortization_months))) / ((1 + Emr) ** amortization_months -1)

    print(f"Monthly Payment amount is: ${monthly_payment:.0f}")


    view_amortization = input("Would you like to see the amortization schedule? (Y/N): ").lower()
    while view_amortization != "y" and view_amortization != "n":
        view_amortization = input("Would you like to see the amortization schedule? (Y/N): ").lower()

    if view_amortization == "y":
        print(f"{'Monthly Amortization Schedule':>54}")
        print("")
        print(f"Month{'Opening Bal':>15}{'Payment':>15}{'Principal':>15}{'Interest':>15}{'Closing Bal':>15}")

        balance = principal_amount
        total_principal = 0
        total_interest = 0

        for m in range(term * 12):

            opening_balance = balance
            monthly_interest = balance * Emr
            monthly_principal = monthly_payment - monthly_interest
            balance -= monthly_principal
            total_principal += monthly_principal
            total_interest += monthly_interest

            print(f"{m + 1:>5}{opening_balance:>15.2f}{monthly_payment:>15.2f}{monthly_principal:>15.2f}{monthly_interest:>15.2f}{balance:>15.2f}")
        print("=" * 80)
        print(f"Total{total_principal:>45.2f}{total_interest:>15.2f}")

if __name__ == "__main__":
    main()