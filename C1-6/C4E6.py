def inputparameters():
   hours=float(input('Enter hours '))
   rate=float(input('Enter rate '))
   return hours, rate

def computepay(hours, rate):
    salary=0
    hh1=0
    hh2=hours

    if hours > 40:
        hh1 = hours - 40
        hh2 = hours - hh1

    salary = hh1 * rate * 1.5 + hh2 * rate
    print('Pay '+str(salary))

    print (hh1, hh2, hours)

    if hours > 40:
        print('Pay '+str(((hours-40)*(rate*1.5))+40*rate))
    else :
        print('Pay '+str(hours*rate))

hh,rr=inputparameters()
computepay(hh,rr)
