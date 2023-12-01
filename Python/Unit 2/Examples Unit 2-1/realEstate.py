# show running a program in VS Code
current_price = int(input("Enter current price: "))
last_month_price = int(input("Enter last month's price: "))
change_price = current_price - last_month_price
monthly_mortgage = (current_price * 0.051) / 12
print("Summary")
print("Current price:", current_price)
print("Change since last month:", change_price)
print("Estimated monthly mortgage:", monthly_mortgage)