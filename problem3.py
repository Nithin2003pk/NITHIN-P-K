def generate_odd_until(n):
    result = []
    for i in range(1, n+1):
        if i % 2 != 0:
            result.append(i)
    return result
print(generate_odd_until(4))