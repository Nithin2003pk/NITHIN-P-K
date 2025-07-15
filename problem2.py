def generate_odd_series(n):
    result = []
    num = 1
    for _ in range(n):
        result.append(num)
        num += 2
    return result
print(generate_odd_series(4))