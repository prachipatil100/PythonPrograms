
def is_palindrome_string(text):
    text = text.lower()
    reverse = ""

    for char in text:
        reverse = char + reverse

    return text == reverse

if __name__ == "__main__":
    print(is_palindrome_string("radar"))
    print(is_palindrome_string("hello"))