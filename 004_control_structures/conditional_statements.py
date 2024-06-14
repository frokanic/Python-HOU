

"""
There are 2 ways to conditionally execute code in Python, if and match.
Match was added in python at 2021, in version 3.10, so it may not be
present in older books.
"""

def main():
    wish_for_age_milestones()


def sell_alcohol():
    age = int(input("Please enter your age: "))

    if age <= 0:
        print("You cannot be sooo young, you probably made a mistake :/")
    elif age < 18:
        print("No alcohol for you, you're still a baby!")
    elif age < 21:
        print("You're lucky we don't live in the US.")
    else:
        print("Here you go my friend.")


def wish_for_age_milestones():
    age = int(input("Please enter your age: "))

    match age:
        case 0:
            print("You were just born, congrats!")
        case 18:
            print("You just became an adult. Take care!")
        case 67:
            print("Time for retirement. What a life this has been so far!")
        case other:
            print("Meeeeeh...")


if __name__ == "__main__":
    main()
