from os import system
from json import dumps

system("cls")

def func(left: list,right: list,lst):
    countl = 0
    countr = 0
    for i in range(len(lst)):
        if lst[i] in left:
            countl += 1
        if lst[i] in right:
            countr += 1
    a = []
    a.append(countl)
    a.append(countr)
    return a

lefthand = [
    '1','q','a','z','!',
    '2','w','s','x','@',
    '3','e','d','c','#',
    '4','r','f','5','v','t','g','b','%','$'
]
righthand = [
    '6','y','h','n','7','u','j','m','&','^',
    '8','i','k',',','*',
    '9','o','l','.','(',
    '0','p',';',':','/','?',
    '"','[',']','{','}','\'','-','_','=','+',')'
]
matn = list(input("gapni yoki so'zni kiriting : "))
print(matn)

natija = func(lefthand,righthand,matn)
print(natija)