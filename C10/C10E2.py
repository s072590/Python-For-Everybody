try:
    fhand = open(input('Enter file name: '))
except: 
    print ('file not found')

hour = dict()
for line in fhand:
    words = line.split()

    if len(words) > 1 and words[0] == 'From':
        time = words[5]
        atwords = time.split(':')
#        print (atwords)
        domain = atwords[0]
#        person = words[1]
        hour[domain] = hour.get(domain,0) + 1

#print (hour)

lst = list()
for key, val in list(hour.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print (key, val)