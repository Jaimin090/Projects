#dice.py
# Use random module function to simulate rolling of dice
import random
rollAgain = 'Y'
dieTotal = 0
while rollAgain == 'Y': 
    die1 = random.randint(1,6)
    die2 = random.randint(1,6) 
    dieTotal += (die1 + die2)       
    print(f"Die1 = {die1:d} Die2 = {die2:d}")
    rollAgain = input('Do you want to roll again? (Y or N): ').upper()
print('Total of all rolls =', dieTotal)
