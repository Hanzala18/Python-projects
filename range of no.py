class numbers:
    def __iter__(s):
        s.b = 1
        return s

    def __next__(s):
        if s.b <= 50:
            x = s.b
            s.b += 2
            return x
        else:
            raise StopIteration


i = numbers()
myiter = iter(i)

for x in myiter:
    print(x)
