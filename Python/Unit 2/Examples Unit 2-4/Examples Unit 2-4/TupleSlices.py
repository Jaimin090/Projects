#TupleSlices.py
# Just like list slices. There create new tuples.
# startIndex is inclusive
# endIndex is exclusive
nameTuple = ('Joe', 'Ed', 'Fred', 'Joe')
list = nameTuple [0:3]
print (list)
list = nameTuple [:3]
print (list)
nameString = (nameTuple [2])
print (nameString)
list = (nameTuple [2:])
print (list)
list = nameTuple [-3:]  #start from last third value of tuple till the end
print (list)
everyOther = nameTuple [::2]   #start at the beginning, go to the end, and take every second element
print (everyOther)

    