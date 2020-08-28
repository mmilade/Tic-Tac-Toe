random_numbers = str([1, 22, 333, 4444, 55555])
random_numbers = random_numbers.split(",")
print("\n".join(random_numbers).replace("[", "").replace("]", "").replace(" ", ""))

# Another solution
# random_numbers = [1, 22, 333, 4444, 55555]
# print("\n".join(str(i) for i in random_numbers))
