try:
    fhand = open(input('Enter file name: '))
except: 
    print ('file not found')
    exit()

sender = dict()
for line in fhand:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        person = words[1]
        sender[person] = sender.get(person,0) + 1

#print (sender)
lst = list()
for key, val in list(sender.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print (val, key)