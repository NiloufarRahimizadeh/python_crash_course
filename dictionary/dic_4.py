food = {
    "GhormeSabzi": {
        "fried vegtables": "400 grams",
        "meat": "500 gram",
        "beans": "40 gram",
        "verjuice": "2 spoons",
        "pepper and salt": "enough",
    },
    "fried egg": {
        "oil": "4 spoons",
        "egg": "2 numbers",
        "pepper and salt": "enough"
    },
    "roast potato":{
        "potato": "2 numbers",
        "pepper and salt": "enough"
    },
    "french fries":{
        "potato": "2 numbers",
        "oil": "4 spoons",
        "pepper and salt": "enough",
    }
}


for key in food:
    print(key)


user_requst = input("please enter your favorite food: ")

for key in food[user_requst]:
    print(key)

user_requst2 = input("To see details: ")

print(food[user_requst][user_requst2])