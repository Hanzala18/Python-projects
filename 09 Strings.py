
x = "Das ist ein Text, der beste Text der Welt, ja ja der text ist super, quasi ein Supertext!"
such = "Text"

x = x.lower()
x = x.replace(",","")
such = such.lower()
print (x)

print (x.count(such))

woerter = x.split(" ")
#print (woerter)
anzahl = 0
for wort in woerter:
    if wort == such:
        print (wort)
        anzahl = anzahl + 1

print (anzahl)