#DictMethods.py
# Original List
monthDict = {1: 'Jan', 2: 'Feb', 3: 'Mar'}
# using get
mon = monthDict.get(3)
month = monthDict.get(4,'NA')
print (mon)
print (month)
# using update
monthDict.update ({4: 'Apr'})
print (monthDict)
# using pop
mon = monthDict.pop(1)
print (mon)
print ('Updated list')
print (monthDict)
#using clear
monthDict.clear()
print (monthDict)
