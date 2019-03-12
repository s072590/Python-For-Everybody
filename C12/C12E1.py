import socket

webinp = input('Enter a website: ')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

webcon = webinp.split('/')
if webinp.startswith('http'):
    for p in webcon:
        part = webcon[2]
if not webinp.startswith('http'):
    for p in webcon:
        part = webcon[0]

print('bugfind', part)

str1 = 'GET '
str2 = webinp
str3 = ' HTTP/1.0\r\n\r\n'
str = str1+str2+str3

try:
    mysock.connect((part,80))
    #cmd = u.encode('GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')
    cmd = str.encode()
except:
    print('bad gateway')
    exit()
    
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()