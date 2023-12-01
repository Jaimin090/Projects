# String Slicing
name = 'Joe B. Programmer'
print ('firstName = name[0:3]')
firstName = name[0:3]
print (firstName)

print ('firstName = name[:3]')
firstName = name[:3]
print (firstName)

print ('middleInitial = name[4]')
middleInitial = name[4]
print (middleInitial)

print ('lastName = name[7:]')
lastName = name[7:]
print (lastName)

print ('lastName = name[7:len(name)] ')
lastName = name[7:len(name)] 
print (lastName)

print ('lastName = name[-10:]')
lastName = name[-10:] 
print (lastName)

print ('everyOther = name[::2]')
everyOther = name[::2]
print (everyOther)
