available_toppings = ["Pizza", "grilled fish", "french fries", "boiled egg", "Rice"]
requested_toppings = ["steak", "mashrooms", "grilled fish"]

for request in requested_toppings:
    if request in available_toppings:
        print(f"{request} is already exist.")
    else:
        print(f"Sorry, we don't have {request}")