

def main():
    print("asgag is a pangram: " + str(is_palindrome("asgag")))
    print("A man, a plan, a canal, Panama is a pangram: " + str(is_palindrome("A man, a plan, a canal, Panama.")))


def is_palindrome(sentence):
    cleaned_sentence = "".join(char for char in sentence if char.isalnum()).lower()
    reversed_sentence = cleaned_sentence[::-1]
    return cleaned_sentence == reversed_sentence


if __name__ == "__main__":
    main()

