#DictFunctions.py
monthDict = {1: 'Jan', 2: 'Feb', 3: 'Mar'}
print (min(monthDict))
print (len(monthDict))
del monthDict[2]
print (monthDict)

monthDict = {'Jan': 1, 'Feb' :2, 'Mar':3}
print (min(monthDict))
print (len(monthDict))
monthDict.clear()
print (monthDict)

