

"""
There are 2 ways to "repeat something" in Python. For and while loops.
"""

def main():
    single_digit_odd_numbers()

def hi_there():
    for _ in range(3):
        print("Hi there :)")

def single_digit_integers_squared():
    for num in range(1, 6):
        print("Number", num, "squared is", num**2)

def single_digit_odd_numbers():
    for num in range(1, 10, 2):
        print("Number", num, "is odd.")


if __name__ == "__main__":
    main()
