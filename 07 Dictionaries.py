x = [1,1,2,3,4,5,4,3,2,3,4,3,2,1,6,2,4,5,1,1,3,4,5,6,4,3,2,1,20]

anzahl={}

for k in x:
    if k in anzahl:
        anzahl[k] = anzahl[k]+1
    else:
        anzahl[k] = 1

for k in anzahl:
    print (k, anzahl[k])
