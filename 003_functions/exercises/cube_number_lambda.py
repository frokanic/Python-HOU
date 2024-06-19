
"""
Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
"""

def main():
    print(cube(int(input("Please insert a number: "))))


cube = lambda num: num **3


if __name__ == "__main__":
    main()

