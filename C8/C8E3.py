fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print ('Debug: ', words)
    if len(words) > 2 and words[0] == 'From' :
#    if words[0] != 'From' : 
        print(words[2])
