try:
    fhand = open(input('Enter file name: '))
except: 
    print ('file not found')

sender = dict()
for line in fhand:
    words = line.split()

    if len(words) > 1 and words[0] == 'From':
        mail = words[1]
        atwords = mail.split('@')
#        print (atwords)
        domain = atwords[1]
#        person = words[1]
        sender[domain] = sender.get(domain,0) + 1

print (sender)

#sndrlist = list(sender.values())
#for key in sndrlist:

#largest = None
#for value in sndrlist:
#    if largest is None or value > largest:
#        largest = value
#    print ('loop:', value, largest)

#for key in sender:
#    if sender[key] == largest:
#        print (key, sender[key])
#        maxsender = key

#print (maxsender, largest)