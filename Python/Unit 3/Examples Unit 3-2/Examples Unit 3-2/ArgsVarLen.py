#ArgsVarLen.py
# the arg is a tuple that is passed in
def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product

print(multiply(2, 3, 7))
# 5!
print (multiply (1,2,3,4,5))