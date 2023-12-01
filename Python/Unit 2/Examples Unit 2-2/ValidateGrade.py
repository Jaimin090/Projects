# check for a valid percentage grade
score = float (input ("Enter percentage: "))
if 0.0 <= score <= 100.0:
    print ("Grade accepted")
else: 
    print ("Invalid grade")
