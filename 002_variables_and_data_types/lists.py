"""
A list is a collection or grouping of items.
    - Lists are ordered.
"""
def main():
    print(check_if_value_in_list("Fotis", names))
    print(check_if_value_in_list("Foti", names))


names = ["Fotis", "George", "Mary", "April"]
first_name = names[0]
last_name = names[-1]

def print_all_names(l):
    for index in range(0, len(l)):
        print(l[index])

def print_all_names_backwards(l):
    for index in range(-1, -len(l) - 1, -1):
        print(l[index])

def check_if_value_in_list(value, l):
    return value in l


if __name__ == "__main__":
    main()