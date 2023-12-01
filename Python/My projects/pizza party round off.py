import math
numPeople = int (input ('How many people? '))
numPizza = math.ceil(numPeople * 2 / 12)
cost = numPizza * 18.75
if (numPizza >= 2):
    cost = cost - (cost *0.10)
print ("# of pizza = ", numPizza, "Cost is $", cost)