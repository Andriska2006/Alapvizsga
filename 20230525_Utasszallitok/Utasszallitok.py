from Utasszallito import Utasszallito

utasszallitok : list[Utasszallito] = []

file = open('utasszallitok.txt', 'r', encoding="utf-8")
file.readline()
for sor in file:
    utasszallitok.append(Utasszallito(sor.strip()))
file.close()

print(f'4. Feladat: Adatsorok száma: {len(utasszallitok)}')

boeingDarab = 0
for item in utasszallitok:
    if 'Boeing' in item.tipus:
        boeingDarab += 1

print(f'5. feladat: Boeing típusok száma: {boeingDarab}')