print("Enter cells: ")
cells = list(input())
for element in cells:
    if element not in "X, O, _":
        print(element, "is a bad character, only X, O, _ characters are allowed")
print(cells)
print("-----------")
print("|", cells[0], cells[1], cells[2], "|",)
print("|", cells[3], cells[4], cells[5], "|",)
print("|", cells[6], cells[7], cells[8], "|",)
print("-----------")
