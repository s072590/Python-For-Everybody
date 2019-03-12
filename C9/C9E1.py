fhand = open('words.txt')
wordie = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in wordie:
            wordie[word] = 0

searching = input('Enter word to search for ')

if wordie.get(searching) == None :
    print ('searched word not in dict')
else :
    print ('yes it was in dict')


#print (wordie)
