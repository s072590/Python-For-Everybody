regex = input('Enter a regular expression: ')

import re
fhand = open('mbox.txt')
#reglist = list()
count = 0
#comp = re.compile(r"regex")
for line in fhand:
    line = line.rstrip()
    reglist = re.findall(regex, line)
    if len(reglist) >= 1:
        count = count + 1

#print (reglist)
print ('mbox.txt had ', count, 'lines that match', regex)
