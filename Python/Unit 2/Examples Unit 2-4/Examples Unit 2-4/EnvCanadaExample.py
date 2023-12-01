#EnvCanadaExample.py
# Env Canada Example
string1 = '-114,51.11,CALGARY INT''L CS,3031094,1/1/2022,2022,1,1,,-0.3,,-26.6,,-13.4,,31.4,,0,,,,,,0,,8,,28,,57,'
list2 = string1.split(',')
print(list2)
max = float(list2[9])
min = float(list2[11])
print ("Max = ", max)
print ("Min = ", min)
