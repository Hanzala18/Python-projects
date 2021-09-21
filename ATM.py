def balance(i):
    print(i)


def deposit(i):
    x = int(input("Enter the amount you want to deposit :\n "))
    print("your amount after deposit is :")
    print(int(i) + int(x))


def transaction(i):
    y = int(input("Enter the amount you want to transact :\n"))
    print("your amount after transaction is :")
    print(int(i) - int(y))


pin = int(input("Please Enter your pin no :\n"))
i = 10000
if pin == 1122:
    print("WELCOME")
    print("Following are our services ")
    print("Press 1 to check your current account balance")
    print("Press 2 for deposit")
    print("press 3 for transaction")
    start = int(input("Enter your option\n"))

    if start == 1:
        balance(i)

    elif start == 2:

        deposit(i)
    elif start == 3:

        transaction(i)
    else:
        print("Invalid option")
else:
    print("Invalid pin")

    # another = int(input("Enter for another program\n")
    #         print("Press 1 for another transaction")
    #         print("press 2 to finish")
    #         if another == 1:
    #             another == start
    #         else:
    #             print("Thankyou")

print("Thankyou")
exit()
