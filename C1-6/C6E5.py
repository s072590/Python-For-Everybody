str = "X-DSPAM-Confidence:0.8475"

colonpos = str.find(":")
print (colonpos)

strslice = str[colonpos+1:]
print (strslice)

finalnr = float(strslice)
print (finalnr)