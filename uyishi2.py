from os import system
from json import dumps

system("cls")

def bigger_price(son: int,lst: list):
    for i in range(len(lst)):
        for j in range(i + 1,len(lst)):
            if lst[i]['price'] < lst[j]['price']:
                lst[i]['price'], lst[j]['price'] = lst[j]['price'], lst[i]['price']

    for i in range(son):
        print(lst[i])


son = int(input("son = "))
lst = [
    {
        "name": "bread",
        "price": 100
    },
    {
        "name": "wine",
        "price": 138
    },
    {
        "name": "meat",
        "price": 15
    },
    {
        "name": "water",
        "price": 1
    }
]
# print(dumps(lst , indent = 2))
bigger_price(son,lst)