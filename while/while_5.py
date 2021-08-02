list_numbers = list(range(1, 50))
p
rint(list_numbers)
new_list = []
while list_numbers:
    item = list_numbers.pop(0)
    if item%7:
        continue
    new_list.append(item)

print(new_list)
