text = input()
text = text.split("_")
text = [i.capitalize() for i in text]
text = "".join(text)
print(text)




# Other solutions
# name = input().split('_')
# name = [x.capitalize() for x in name]
# print(''.join(name))

# ---------
# text = input()
# print(text.replace('_', ' ').title().replace(' ', ''))
