#Random.py
import random
print ('random.random()')
print(random.random())

print ('random.randint(1, 10)')
print (random.randint(1, 10))
print ('random.randrange(0, 30, 3)')
print (random.randrange(0, 30, 3))
print ('random.uniform(1.0, 10.0)')
print (random.uniform(1.0, 10.0))
print ('random.choice(dice)')
dice = [1, 2, 3, 4, 5, 6]
x = random.choice(dice)
print (x)
print ('Set a seed')
print ('random.seed(23709)')
random.seed(23709)
print ('random.randint(1, 10)')
print (random.randint(1, 10))
print ('random.randint(1, 10)')
print (random.randint(1, 10))


