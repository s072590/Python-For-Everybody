try:
    fhand = open(input('Enter file name: '))
except: 
    print ('file not found')
    exit()

letters = dict()
import string
from string import digits
for line in fhand :
#    if len(line) > 0
        line = line.rstrip()
        line = line.translate(line.maketrans('','',string.punctuation))
#        line = line.translate(line.maketrans("","",digits))
        line = line.lower()
        words = line.split()
        for word in words :
            for c in word :
                if not c.isdigit():
                    letters[c] = letters.get(c, 0) +1

lst = list()
for key, val in list(letters.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst :
    print (key, val)

#print (letters)