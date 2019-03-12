#import socket

webinp = input('Enter a website: ')


import urllib.request
try:
    fhand = urllib.request.urlopen(webinp)
except:
    print('bad gateway')
    exit()


info = fhand.read(3000)

dec = info.decode()

print(dec,'length of text ',len(dec))

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#webcon = webinp.split('/')
#if webinp.startswith('http'):
#    for p in webcon:
#        part = webcon[2]
#if not webinp.startswith('http'):
#    for p in webcon:
#        part = webcon[0]

#print('bugfind', part)

#str1 = 'GET '
#str2 = webinp
#str3 = ' HTTP/1.0\r\n\r\n'
#str = str1+str2+str3

#try:
#    mysock.connect((part,80))
#    #cmd = u.encode('GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')
#    cmd = str.encode()
#except:
#    print('bad gateway')
#    exit()
    
#mysock.send(cmd)

#data = mysock.recv(3000)

#datadec=data.decode()

#print(data.decode(),end='')

#print('\n nr of chars ',len(data.decode()))

#mysock.close()