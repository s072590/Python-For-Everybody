fhand = open('mbox-short.txt')
wordlist = []
count = 0
for line in fhand:
    splitted = line.split()
    if len(splitted) <= 1 : continue
    if splitted[0] != 'From' : continue
    count = count + 1
    print (splitted[1])

print ('There were', count, 'lines in the file with From as the first word')

#    for word in splitted:
#        if word in wordlist:
#            continue
#        else:
#            wordlist.append(word)

#wordlist.sort()
#print(wordlist)