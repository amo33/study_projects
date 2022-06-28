longstring = input()
maxlen = len(longstring)
startloc = 0 
endloc = 10
while startloc < maxlen:
    if endloc > maxlen:
        print(longstring[startloc:maxlen])
    else:
        print(longstring[startloc:endloc])
    startloc = endloc 
    endloc += 10  