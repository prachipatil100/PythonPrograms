def reverse_string(text):
    reverse =""

    for char in text:
        reverse = char + reverse

    return reverse

if __name__ == "__main__":
    print(reverse_string("hello"))