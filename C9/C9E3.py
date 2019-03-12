try:
    fhand = open(input('Enter file name: '))
except: 
    print ('file not found')

sender = dict()
for line in fhand:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        person = words[1]
        sender[person] = sender.get(person,0) + 1

print (sender)