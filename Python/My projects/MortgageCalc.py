name = input("Enter client name: ")
address = input("Enter address of property: ")
purchase_price = int(input("Enter purchase price: "))
percentage_downpay = int(input("Enter down payment percentage: "))

while not (5<= percentage_downpay <100):   # making sure if the input percentage is between 5 and 99
    print("Please enter a value between the minimum and 100")
    percentage_downpay = int(input("Enter down payment percentage: "))
    
if purchase_price <= 500000 :              # blocks for calculating downpayment, minimum downpayment and percentage for different purchase prices 
    min_downpay = purchase_price * 0.05    
             
elif purchase_price <=1000000:
    min_downpay = 500000 * 0.05 + (purchase_price - 500000) * 0.1
    min_percentage = (min_downpay/purchase_price) * 100     # the min percentage is still left to put in the input as per the final output
    print(min_percentage)

else:
    while not (20<= percentage_downpay <100):      # learned to put while loop in else statement using ChatGPT
        print("Please enter a value between the minimum and 100")
        percentage_downpay = int(input("Enter down payment percentage: "))
    min_downpay = purchase_price * 0.2

downpayment = purchase_price * (percentage_downpay/100)    # final downpayment
print("Down payment amount is $",downpayment)

if percentage_downpay < 10:     # if block for getting the mortgage insurance premium rate according to the percentage for downpayment
    mortgage_premium = 4
elif percentage_downpay < 15:
    mortgage_premium = 3.1
elif percentage_downpay < 20:
    mortgage_premium = 2.8
else:
    mortgage_premium = 0

insurance_cost = (purchase_price - downpayment) * mortgage_premium/100
print("Mortgage insurance price is $", insurance_cost)

principal_amount = purchase_price - downpayment + insurance_cost
print("Total mortgage amount is $", principal_amount)

valid_terms = [1,2,3,5,10]
term = int (input ('Enter mortgage term (1, 2, 3, 5, 10): '))
while term not in valid_terms:
    print ('Please enter a valid choice')
    term = int (input ('Enter mortgage term (1, 2, 3, 5, 10): '))
mortgage_rates = {1:5.95, 2:5.9, 3:5.6, 5:5.29, 10:6}
intrest_rate = mortgage_rates[term]
print ('Rate is', intrest_rate)                 #

valid_amortization = [5, 10, 15,20, 25]
amortization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
while amortization not in valid_amortization :
    print ('Please enter a valid choice')
    amortization = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
power = 1/12                            # for some reason 1/12 directly put in Emr desnt work
Emr = (((1 + intrest_rate/200) ** 2) ** power) - 1      # Emr is the Effective Monthly Rate
amortization_mnths = amortization * 12
monthly_payment = principal_amount ((Emr (1 + Emr)) ** amortization_mnths) / ((1 + Emr) ** amortization_mnths) -1
