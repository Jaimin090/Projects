#TupleFunctions.py
# Same as lists except for del – can only delete entire tuple
nameTuple = ('Joe', 'Ed', 'Fred')
num = len(nameTuple)
print (num)
first = min(nameTuple)
print (first)
print (max(nameTuple))  # E F and then J so Joe, if same the go for nxt alphabet
del nameTuple
print (nameTuple) #generates error message

