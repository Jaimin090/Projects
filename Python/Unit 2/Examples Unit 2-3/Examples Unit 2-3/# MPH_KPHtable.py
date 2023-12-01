# MPH to KPH table
MILES_TO_KM = 1.61
print (format("MPH", "10s"), format("KPH", "10s"))
print("="*20)
for mph in range (10, 71, 10):
    kph = mph * MILES_TO_KM
    print (format(mph, "10d"), format(kph, "10.0f"))
                     # OR #
   # print(f'{mph:>10.0f}{kph:>10.0f}') # Chat GPT