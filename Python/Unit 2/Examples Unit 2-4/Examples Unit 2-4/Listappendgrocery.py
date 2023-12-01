list = []
item = (input("Enter grocery item ('quit’ to exit): "))
while item == 'quit':
    list.append(item)
    item = (input("Next item: "))   
print("Here is the grocery list: ")
print(list)
