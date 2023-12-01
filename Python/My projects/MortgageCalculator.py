# CPRG 216-J Assignment 2 - Programming Strategies
# Jaimin Chavda, Michael (Zi) Liang, Aman Sharma (Oregano), SAIT, 
# Nov 2, 2023

def minimum_percentage(purchase_price):
    """        
    Function to calculate minimum down payment, in percent, given purchase price.

    Args:
        purchase_price - purchase price of mortgage, before down payment, interest, and insurance.

    Returns:
        The minimum down payment percentage.
    """
    if purchase_price <= 500000:
        return 5.000             # 5% for <= 500,000
    elif purchase_price > 1000000:
        return 20.000              # 20% for > 1,000,000
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
    #Get client name and address
    name = input("Enter client name: ")
    address = input("Enter address of property: ")

    #Get raw purchase price (whole dollar only) and down payment percentage, based on calculated minimum
    purchase_price = int(input("Enter purchase price: "))                        
    percentage_downpay = float(input(f"Enter down payment percentage (minimum {minimum_percentage(purchase_price):.3f}): "))

    # This while loop continues to run until a valid percentage is entered
    while (not minimum_percentage(purchase_price) <= percentage_downpay < 100):      
        print("Please enter a value between the minimum and 100")
        percentage_downpay = float(input(f"Enter down payment percentage (minimum {minimum_percentage(purchase_price):.3f}): "))
        # (i.e, between minimum percentage required for the purchase price and 100%)
        # else:                                                                          
        # print(f"Down payment percentage: {percentage_downpay:.0f}%")

    # Look up mortgage insurance premium percentage according to down payment percentage
    if percentage_downpay < 10:     
        mortgage_premium = 4
    elif percentage_downpay < 15:
        mortgage_premium = 3.1
    elif percentage_downpay < 20:
        mortgage_premium = 2.8
    else:
        mortgage_premium = 0

    downpayment = purchase_price * (percentage_downpay/100)    # Calculate down payment in dollars based on purchase price and percentage
    print(f"Down payment amount is ${downpayment:.0f}")

    insurance_cost = (purchase_price - downpayment) * mortgage_premium/100     # Calculate insurance in dollars using the Mortgage Insurance Premium rate
    print(f"Mortgage insurance price is ${insurance_cost:.0f}")

    principal_amount = purchase_price - downpayment + insurance_cost    # Final principal amount, in dollars, after down payment, insurance, interest
    print(f"Total mortgage amount is ${principal_amount:.0f}")


    mortgage_rates = {1:5.95, 2:5.9, 3:5.6, 5:5.29, 10:6}       # Dictionary of interest rates based on term
    term = int (input ('Enter mortgage term (1, 2, 3, 5, 10): '))
    while term not in mortgage_rates :
        print ('Please enter a valid choice')
        term = int (input ('Enter mortgage term (1, 2, 3, 5, 10): '))
    intrest_rate = mortgage_rates[term]          


    valid_amortization = [5, 10, 15, 20, 25]     # Array of valid amortization period for user to choose from. Code is similar to the block above
    amortization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
    while amortization not in valid_amortization :
        print ('Please enter a valid choice')
        amortization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
        
    print (f"Intrest rate for the term will be {intrest_rate:.2f}%")           

    power = 1/12      # for some reason 1/12 directly put in Emr desnt work
    Emr = (((1 + intrest_rate/200) ** 2) ** power) - 1      # Emr is the Effective Monthly Rate
    amortization_months = amortization * 12
    monthly_payment = principal_amount * ((Emr * ((1 + Emr) ** amortization_months))) / ((1 + Emr) ** amortization_months -1)

    print(f"Monthly Payment amount is: ${monthly_payment:.0f}")

    # Ask user whether to show amortization schedule
    view_amortization = input("Would you like to see the amortization schedule? (Y/N): ").lower()
    while view_amortization != "y" and view_amortization != "n":
        view_amortization = input("Would you like to see the amortization schedule? (Y/N): ").lower()

    if view_amortization == "y":
        # Display headings
        print(f"{'Monthly Amortization Schedule':>54}")
        print("")
        print(f"Month{'Opening Bal':>15}{'Payment':>15}{'Principal':>15}{'Interest':>15}{'Closing Bal':>15}")

        # Prepare variables to be modified: balance (start of month), cumulative principal paid, cumulative interest paid
        balance = principal_amount
        total_principal = 0
        total_interest = 0


        for m in range(term * 12):
            # Formulas for monthly payment, monthly principal, monthly interest, closing balance
            # Also updates running balance for next month's calculations
            opening_balance = balance
            monthly_interest = balance * Emr
            monthly_principal = monthly_payment - monthly_interest
            balance -= monthly_principal
            total_principal += monthly_principal
            total_interest += monthly_interest

            # Display one month of info
            print(f"{m + 1:>5}{opening_balance:>15.2f}{monthly_payment:>15.2f}{monthly_principal:>15.2f}{monthly_interest:>15.2f}{balance:>15.2f}")

        # Display divider and total principal and interest paid
        print("=" * 80)
        print(f"Total{total_principal:>45.2f}{total_interest:>15.2f}")

if __name__ == "__main__":
    main()