daily_works = []


while True:
    print("If you want to close your list, please enter 'q'")
    inp1 = input("Enter your daily work: ")
    if inp1=="q":
        break
    daily_works.append(inp1)
    print(daily_works)