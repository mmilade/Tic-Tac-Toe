text = input()
new_text = ""

for char in text:
    if char in ",.!?":
        pass
    else:
        new_text = new_text + char

new_text = new_text.lower()

print(new_text)


# Other solutions:
#
# sentence = input()
# for i in ['!', '.', ',', '?']:
#     sentence = sentence.replace(i, '')
# print(sentence.lower())
#
# ---------
#
# print(input().translate(str.maketrans('', '', ',.!?')).lower())
#
# ---------------
# sentance = input().lower()
#
# sentance2 = sentance.replace("!", "").replace("?", "").replace(".", "").replace(",", "")
#
# print(sentance2)
