count = 0
total = 0
largest_so_far = float('-Inf')
smallest_so_far = float('Inf')

print('Before', total, count, largest_so_far, smallest_so_far)

while True:

    line = input('> ')
    if line == 'done':
        break
    try:
        line = float(line)

        count = count + 1
        total = total + line
        if line > largest_so_far:
            largest_so_far = line
        if line < smallest_so_far:
            smallest_so_far = line
        print(line, total, count, largest_so_far, smallest_so_far)
    except:
        print('invalid input') 
if count != 0:
    print('After', total, count, largest_so_far, smallest_so_far)
else: 
    print('count = 0')
