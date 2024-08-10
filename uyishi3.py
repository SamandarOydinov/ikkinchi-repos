from os import system
from json import dumps

system("cls")

def func(son):
    count = 0
    for i in range(len(son)):
        if son[i] != '0':
            return count
        count += 1

son = input("sonni kiriting : ")

natija = func(son)
print(natija)