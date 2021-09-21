def greet():  # simple function
    print("Hii Hanzala Hashmi")


greet()


def greet(first_name, last_name):  # function with argument
    print(f"Hii {first_name}{last_name}")
    print("Welcome to aboard")


greet("Hanzala", "Hashmi")


def increment(number, by):  # arguments by print
    return number + by


result = increment(9, 5)
print(result)


def increment(number, by):  # arguments by print
    return number + by


print(increment(9, 5))


def multiply(*numbers):  # arguments with mutiple values
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply(2, 3, 5, 6, 8))


def save_user(**user):
    print(user)


save_user(id=2, age=25, name="Hanzala")
