def get_second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]

if __name__ == "__main__":
    print(get_second_largest([10, 20, 4, 45, 99]))
