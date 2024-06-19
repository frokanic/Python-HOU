"""
Write a function called decrement_list  that accepts a single list of numbers
as a parameter.  It should return a copy of the list where each item has
been decremented by one.
"""
def main():
    print(decrement_list([1, 2, 3]))


def decrement_list(l):
    return list(map(lambda num: num - 1, l))


if __name__ == "__main__":
    main()
