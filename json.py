import re
a = "The game was stop by the rain"
x = re.search("^The.*rain$", a)
if x:
    print("Yes! but it will resume soon")
else:
    print("The game is on")

x = re.split("\s", a)
print(x)

x = re.sub("\s", "   ", a)
print(x)
