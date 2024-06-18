"""
Write a Python function to check whether a sentence is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
"""

def main():
    print("asgag is a pangram: " + str(is_pangram("asgag")))
    print("The quick brown fox jumps over the lazy dog is a pangram: "
          + str(is_pangram("The quick brown fox jumps over the lazy dog."))
          )


def is_pangram(sentence):
    return set(sentence.lower()) >= set('abcdefghijklmnopqrstuvwxyz')


if __name__ == "__main__":
    main()

    