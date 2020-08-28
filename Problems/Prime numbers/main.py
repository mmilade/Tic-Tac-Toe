prime_numbers = [x for x in range(2, 100000) if all(x % y for y in range(2, x))]
print(prime_numbers)