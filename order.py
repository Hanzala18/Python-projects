print("Place your order")
print("Burger = 300 ")
print("fries = 100 ")
print("Pizza = 500 ")

# order = 0
b = 300
f = 100
p = 500
x = input("choose your food\n")
y = input("Enter your quantity\n")


def order(x, y):
    # print()
    if x == "burger":

        print("your amount is :")
        print(int(b) * int(y))
        return b * y
    # return b * y
    elif x == "fries":

        print("your amount is :")
        print(int(f) * int(y))
        return f * y
    elif x == "pizza":

        print("your amount is :")
        print(int(p) * int(y))
        return p * y
    else:
        print("These items are not available")


order(x, y)

exit()
