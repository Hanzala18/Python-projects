print("CALCULATOR")
x = input("Enter the value \n")
y = input("Enter another value \n")


def add(x, y):
    print("value after addition is : ")
    print(int(x) + int(y))  # adding the inputs x and y


def sub(x, y):

    print("value after subtraction is : ")  # subtracting the inputs x and y
    print(int(x) - int(y))


#sub(x, y)


def mult(x, y):

    print("value after multiplication is : ")
    print(int(x) * int(y))  # multiplying the inputs x and y
#mult(x, y)


def divide(x, y):

    print("value after dividion is : ")
    print(int(x) / int(y))  # dividing the value x and y
#divide(x, y)


add(x, y)
sub(x, y)
mult(x, y)
divide(x, y)
exit()
