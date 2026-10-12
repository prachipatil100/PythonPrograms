def char_frequency(text_input):
    freq = {}

    for char in text_input:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

if __name__ == "__main__":
    print(char_frequency("test"))