
def find_missing_number(numbers):
    for i in range(len(numbers) + 1):
        if i not in numbers:
            return i
if __name__ == "__main__":
    print(find_missing_number([1, 2, 4, 5, 6], 6))