try:
    fhand = open(input('Enter file name: '))
except:
    print('file not found')

days = dict()
for line in fhand: 
    daylist = line.split()
    if len(daylist) > 2 and daylist[0] == 'From' :
        specday = daylist[2]
        days[specday] = days.get(specday,0) + 1

print(days)
