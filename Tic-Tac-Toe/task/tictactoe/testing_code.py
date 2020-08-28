# text = input()
# text = text.replace("o", " ")
# text = text.split()
# text = " o".join(text)
# print(text)




print("Enter the coordinates:")
user_input = input()
coordinates = list(user_input.split())
print(coordinates)
options = [
['1', '3'], ['2', '3'], ['3', '3'],
['1', '2'], ['2', '2'], ['3', '2'],
['1', '1'], ['2', '1'], ['3', '1']]

if coordinates in options:
    print("good")
    coordinate_index = options.index(coordinates)
    print(coordinate_index)
else:
    print("bad")