#SetOperator2.py
nameSet = {'Joe', 'Ed', 'Fred'}
otherSet = {'Jack', 'Ed'}
# update, union of current set and specified set
newSet = nameSet
newSet.update(otherSet)
print (newSet)
# remove
newSet = nameSet
nameSet.remove('Fred')
print (nameSet)
# <=
print ({'Joe', 'Ed'} <= nameSet)
# >=
print (nameSet >= {'Joe', 'Jill'})
