from random import randint
from math import sqrt

def ez_prím(szam):
    for i in range(2, round(sqrt(szam))):
        if szam % i == 0:
            return False
    return True

szamok = []

for i in range(10):
    szamok.append(randint(10, 99))

print(szamok)

for item in szamok:
    if ez_prím(item):
        print('Van prímszám a listában.')
        break
else:
    print('Nincs prímszám a listában.')