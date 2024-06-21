

"""
Write a function called remove_negatives that accepts a list of numbers
and returns a copy of the lists with all negative numbers removed.
"""
def main():
    print(remove_negatives([3, 1, -4, 2, 0, -999]))


def remove_negatives(numbers):
    return list(filter(lambda num: num >= 0, numbers))


if __name__ == "__main__":
    main()