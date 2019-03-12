import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

fhand = urllib.request.urlopen(input('Enter url- '))

info = fhand.read()
#print(info)
#print (type(info))
info2 = info.decode()
#print (type(info2))
stuff = ET.fromstring(info2)
#print (stuff)
#print(stuff)
#for line in fhand:
#    print(line.decode().strip())

#dec = info.decode()
#print (dec)

counts = stuff.findall('.//comment')
sums =[]
#print (counts)
#intlist = [int(i) for i in counts]
count = 0
for c in counts:
    sums.append(int(c.find('count').text))
    count = count + int(c.find('count').text)
    #print('count', c.find('count').text)
    #count = count + c
#print (count)
print(sum(sums))
#print ('comment count = ', sum(intlist))
