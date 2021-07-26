names = ["Arnika", "Arvin", "Kamand", "Erfan"]


while names:
    print(names.pop())


while True:
    inp = input("please enter your name: ")
    if inp == "q":
        break
    print(f"Hello {inp}!")