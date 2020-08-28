# prints a running average for given numbers via input
# i.e. input = 12345
# output  = [1.5, 2.5, 3.5, 4.5]

numbers = input()

running_average = [((int(numbers[i]) + int(numbers[i + 1])) / 2) for i in range(len(numbers) - 1)]

print(running_average)