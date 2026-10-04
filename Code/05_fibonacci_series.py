def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    print(generate_fibonacci(6))
