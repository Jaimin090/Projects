TerritoryTuple = ('Northwest Territories', 'Yukon', 'Nunavut')
TerritoryDict = {}

for territory in TerritoryTuple:                  # ask input by loops(as per mr dave), can be done in 2nd way:- go to Projects,Python,TerritoryPopulation2
    population = int(input(f"Enter Population For {territory}: "))
    TerritoryDict[territory] = population         # ChatGPT used for adding key-values in dictionary,thus territory taken as key and population as value after every loop

print(" ")
print("Territory" f"{'Population':>32}")
total = 0                                         # another for loop not needed as total can be calculated in this loop only
print("=" * 41)

for territory,num in TerritoryDict.items():       # (#IMP).items() allows the usage of key and values of tuple from a dictionary (reference DictLoop program)
    print (f"{territory:<21} {num:>19,}")         # semicolon in the outputs is also told by ChatGPT 
    total += num
print("=" * 41)
print("Total" f"{total:>36,}")

#use DictLoop problem for final output and then do sum 