#EnvCanadaData.py
fileName = input("Enter the filename: ")
inFile = open(fileName, 'r')

#read in header information
inFile.readline()
numMaxDays = 0 
numMinDays = 0
totalMaxTemps = 0
totalMinTemps = 0
# while more data

for line in inFile:
    items = line.rstrip().split(',')
    year = int(items[5])
    month =int(items[6])
    day = int(items[7])

    # get max temp
    tempS = items[9] 

    #Check to see if a max temperature is present

    if tempS !='':
        # temperature present convert to double
        maxTemp = float(tempS)
        totalMaxTemps += maxTemp
        numMaxDays += 1

    tempS = items[11]
    if tempS != '':
    # temperature present convert to float
        minTemp = float(tempS)
        totalMinTemps += minTemp
        numMinDays += 1

inFile.close()

# Calculate average maximum
average = totalMaxTemps/numMaxDays

print(f'{"# of days Max Temp reported = ":s}{numMaxDays:d}')
print(f'{"The average maximum temperature is ":s}{average:.2f}')

#calculate average minimum
average = totalMinTemps/numMinDays
print(f'{"# of days Min Temp reported = ":s}{numMinDays:d}')
print(f'{"The average minimum temperature is ":s}{average:.2f}')
