def main():
    print(factorial(5))


def factorial(number):
    result = 1

    if number > 1:
        return result * number * factorial(number - 1)
    return result


if __name__ == "__main__":
    main()

