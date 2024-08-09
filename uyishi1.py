from os import system
from json import dumps
system("cls")

son = int(input("son = "))
strson = str(son)
raqamlar = []
Count = []

while son:
    a = son % 10
    if not a in raqamlar:
        raqamlar.append(a)
        Count.append(strson.count(str(a)))
    son //= 10
dct = {}

for i in range(len(raqamlar)):
    for j in range(i + 1,len(raqamlar)):
        if raqamlar[i] > raqamlar[j]:
            raqamlar[i], raqamlar[j] = raqamlar[j], raqamlar[i]
            Count[i],Count[j] = Count[j], Count[i]

print(raqamlar)
print(Count)
for i in range(len(raqamlar)):
    dct[raqamlar[i]] = Count[i]
print(dumps(dct,indent = 2))