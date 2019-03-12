fname = input('Enter the file name: ')
if fname == 'na na boo boo' :
    print ('NA NA BOO BOO TO YOU - you have been punk\'d!')
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    exit()

count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        conf = float(line[20:26])
        count = count + 1
        total = total + conf

print('Average spam confidence ', total/count)