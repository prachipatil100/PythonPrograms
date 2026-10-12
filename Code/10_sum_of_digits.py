def sum_of_digits(num):
    num = abs(num)
    total = 0

    for digit in str(num):
        total +=int(digit)

    return total

if __name__ == "__main__":
    print(sum_of_digits(1234))
    print(sum_of_digits(-78))
