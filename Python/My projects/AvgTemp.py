templist = []
temperature = float(input("Enter Temperature:"))

while temperature != 999:              # Logic:- AppendGroceryList(class)
    templist.append(temperature)
    temperature = float(input("Enter Temperature:"))

sum =0                      
for temp in templist:
    sum += temp              # numerator of Avg temp
lengthlist = len(templist)      # denominator of Avg Temp

averagetemp = sum/lengthlist # Avg temp

num = []
for temp in templist:                # Logic in line 16 and 17 are helped by ChatGPT 
    if temp > averagetemp:
        num.append(temp)

aboveavg = len(num)
print(f"{aboveavg} temperatures were above the average temperature of {averagetemp:.1f}")