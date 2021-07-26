tick = True
while tick:
    inp = input("please enter your name: ")
    if inp == "q":
        tick=False
    print(f"Hello {inp}!")