#ElectricityFormat.py
print(format(12345.6789, ".2f"))
mon = 5
print ("Enter electricity usage for month", mon, "enter kwh:", end='')
kwh = float ( input())
price_elect = kwh * 0.0097
print ("Price of electricity is $", format(price_elect, ".2f"), sep = '')
