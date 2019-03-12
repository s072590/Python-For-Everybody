    fhand = open('romeo.txt')
wordlist = []
for line in fhand:
    splitted = line.split()
    for word in splitted:
        if word in wordlist:
            continue
        else:
            wordlist.append(word)

wordlist.sort()
print(wordlist)