

def main():
    order_pizza("large", "pepperoni", "olives", delivery = True, tip = 5)


def greet():
    print("Hello my friend!")


def greet_personally(name):
    print("Hello,", name, "!")


def increment(num, by = 1):
    return num + by


"""
args allow us to pass an undefined number of arguments in python
"""

def print_numbers(*numbers):
    for num in numbers:
        print(num)


"""
kwargs allow us to pass an undefined amount of key-value pairs in python.
"""
def order_pizza(size, *toppings, **details):
    print(f"You ordered a {size} pizza with the following toppings:")

    for topping in toppings:
        print(f" - {topping}")

    print("\n Details of the order are:")

    for key, value in details.items():
        print(f" - {key}: {value}")


if __name__ == "__main__":
    main()
