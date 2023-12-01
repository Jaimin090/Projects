# continueExample
sum = 0
for number in range(10):
    if number == 5 or number == 7:
        continue
    sum += number
print(number, end=' ')
