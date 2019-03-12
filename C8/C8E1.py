numbers = [1, 2, 3, 4, 5]

#print(type(numbers))

def chop(t):
    del t[0]
    del t[len(t)-1]
    return None

chop(numbers)

print(numbers)

twombers = [1, 2, 3, 4, 5]

def middle(t):
    return t[1:len(t)-1] 
#    return threembers

threembers = middle(twombers)
print (twombers)
print(threembers)
