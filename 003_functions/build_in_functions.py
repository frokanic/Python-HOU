

"""
Kotlin, much like other languages, has a plethora of build in function.
"""

def main():
    print(instructors_with_short_names)


"""map"""
nums = [2, 4, 6, 8, 10]
doubles = list(map(lambda num: num * 2, nums))

people = ["Darcy", "Christiana", "Dana", "Annabel"]
peeps = list(map(lambda name: name.upper(), people))


"""filter"""
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda num: num % 2 == 0, nums2))

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "godda", "tweets": []},
    {"username": "guigal", "tweets": ["I love cake", "I love my cat"]}
]
inactive_users = list(filter(lambda u: not u["tweets"], users))

names = ["Lassie", "Colt", "Rusty"]
instructors_with_short_names = list(
    map(
        lambda name: f"Your instructor is {name}"
        ,filter(lambda name: len(name) < 5, names)
    )
)

"""any and all"""
# TODO: They are related to list comprehension. Will fill later!




if __name__ == "__main__":
    main()

