name = input("Please enter a text: ")
name = name.lower()
index = name.find("m")
if index==0:
    print(f"{name} starts with m.")
else:
    print(f'{name} doesn\'t starts with m.')


name8 = "maryam"
print(name8.rfind("m"))
print(10 * '-')