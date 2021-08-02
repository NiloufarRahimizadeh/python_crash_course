sentences = "I go to school by bus."

list_1 = sentences.split(" ")


new_list = []
while list_1:
    item = list_1.pop(0)
    f_item = item.title()
    new_list.append(f_item)

print(new_list)
