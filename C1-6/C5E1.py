count = 0
total = 0

print('Before', total, count)

while True:

    line = input('> ')
    if line == 'done':
        break
    try:
        line = float(line)

        count = count + 1
        total = total + line
        print(line, total, count)
    except:
        print('invalid input') 
if count != 0:
    print('After', total, count, total/count)
else: 
    print('count = 0')
