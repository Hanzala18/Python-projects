start = int(input("Enter the start of range:\n"))
end = int(input("Enter the end of the range:\n"))
for x in range(start, end + 1):
    if x % 2 != 0:
        print(x)
