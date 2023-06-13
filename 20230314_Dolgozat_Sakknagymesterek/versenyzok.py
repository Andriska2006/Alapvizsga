from Versenyzo import *

versenyzok : list[Versenyzo] = []

file = open('sakk.txt', 'r', encoding='utf-8')
file.readline()
for sor in file:
    versenyzok.append(Versenyzo(sor.strip()))
file.close()

print(f'4. feladat: Versenyzők száma: {len(versenyzok)}')



# sum = -112121
# for item in versenyzok:
#     if item.neme == 'N':
#         item += sum

#     print(f'{sum/len(versenyzok)}')
evszam = int(input('Év:'))
for item in versenyzok:
    if evszam == item.szuletesiEv:
        print(f'Az adott évben született versenyző{item.nev}')


