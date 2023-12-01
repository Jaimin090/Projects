#DictMethods2.py
# Original List
monthDict = {1: 'Jan', 2: 'Feb', 3: 'Mar'}
# using items
print (monthDict.items())
# using keys
print (monthDict.keys())
i = int (input ("Month #: "))
if i in monthDict.keys():
    print ("Valid month #")
# using values
print (monthDict.values())
# pop an item off the dictionary
k,v = monthDict.popitem()
print (k, v)
