from Eredmeny import Eredmeny

eredmenyek : list[Eredmeny] = []

file = open('ub2017egyeni.txt','r',encoding='utf-8')
file.readline()
for row in file:
    eredmenyek.append(Eredmeny(row.strip()))
file.close()

print(f'3.2 feladat: Futók száma: {len(eredmenyek)}')

noiDarab = 0
for item in eredmenyek:
    if item.kategoria == 'Noi' and item.szazalek == 100:
        noiDarab += 1
print(f'3.3  feladat: Célba érkező női sportolók: {noiDarab} fő')

leghosszabbNevuFuto = eredmenyek[0]
for item in eredmenyek:
    if len(item.nev) > len(leghosszabbNevuFuto.nev):
        leghosszabbNevuFuto = item
print('3.4 feladat: A leghosszabb nevű futó')
print(f'\tNév: {leghosszabbNevuFuto.nev}')
print(f'\tRajtszám: {leghosszabbNevuFuto.rajtszam}')
print(f'\tEredmény: {leghosszabbNevuFuto.ido}')

ferfiOsszIdo = 0
ferfiDarab = 0
for item in eredmenyek:
    if item.kategoria == 'Ferfi' and item.szazalek == 100:
        ferfiOsszIdo += item.idoOraban
        ferfiDarab += 1
print(f'3.5 feladat: Férfi sportolók átlagos ideje: {ferfiOsszIdo/ferfiDarab} óra')