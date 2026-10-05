def primes_in_range(start, end):
    result = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(num)
    return result

if __name__ == "__main__":
    print(primes_in_range(1, 15))
