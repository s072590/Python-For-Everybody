hours=float(input('Enter hours '))
rate=float(input('Enter rate '))
if hours > 40:
	print('Pay '+str(((hours-40)*(rate*1.5))+40*rate))
else :
	print('Pay '+str(hours*rate))