# note all values MUST be integers
start = int(input("Range start: "))
stop = int(input("Range stop: "))
step = int(input("Range step: "))
for i in range(start, stop, step): # step is used to print a value in range after some digits 
    print(i, end=' ')
