import re
numbers = list()

try:
    fhand = open(input('Enter file name: '))
except: 
    print ('file not found')
    exit()

for line in fhand:
    line = line.rstrip()
    reglist = re.findall('^New Revision:.([0-9.]+)', line)
    if len(reglist) >= 1:
        for nr in reglist:
            numbers.append(float(nr))
#        reglist = float(reglist)
#        numbers.append(reglist)

#print (numbers)
print (sum(numbers)/len(numbers))