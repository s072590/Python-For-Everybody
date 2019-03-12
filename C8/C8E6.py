numberlist = []

while True:
    
    numba = input('Enter a number ')
    if numba == 'done':
        break
    try:
        numba = float(numba)
    except:
        print('something wasnt a number') 
        continue
    numberlist.append(numba)
try:
    print ('max is ', max(numberlist), 'min is ', min(numberlist))
except:
    print('something wasnt a number')