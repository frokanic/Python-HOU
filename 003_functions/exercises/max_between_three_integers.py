"""Write a Python function to find the maximum of three numbers."""

def main():
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    num_3 = int(input("Please enter the third number: "))

    print(max_between_three_integers(num_1, num_2, num_3))


def max_between_two_integers(num_1, num_2):
    if num_1 > num_2:
        return num_1
    return num_2


def max_between_three_integers(num_1, num_2, num_3):
    return max_between_two_integers(num_1, max_between_two_integers(num_2, num_3))


if __name__ == "__main__":
    main()

