from Versenyzo import Versenyzo


versenyzok : list[Versenyzo] = []


file = open('torna.csv', 'r', encoding='utf-8')
file.readline()
for sor in file:
    versenyzok.append(Versenyzo(sor.strip()))
file.close()

print('2. feladat')
print(f'Összesen {len(versenyzok)} versenyző indult a versenyen.\n')

print('3. feladat')

max = 0
maxIndex = 0
for i, item in enumerate(versenyzok):
    if item.korlat > max:
        max = item.korlat
        maxIndex = i

print(f'Korláton {versenyzok[maxIndex].nev} szerezte meg az aranyérmet.\n')

print('4. feladat')
rajtszam = int(input('Kérem a versenyző rajtszámát: '))

for item in versenyzok:
    if rajtszam == item.rajtszam:
        print(f'A {rajtszam} rajtszámú versenyző gyűrűn elért eredménye:  {item.gyuru} pont.')
        break

print(f'\n5. feladat\nLólengésben nem jutottak döntőbe:')
for item in versenyzok:
    if item.lolenges < 14.5:
        print(f'\t{item.nev}')

# földrészek : list[str] = []
# for item in versenyzok:
#     if item.foldresz not in földrészek:
#         földrészek.append(item.foldresz)
# földrészek.sort()
# földrészekString = ', '.join(földrészek)
# print(f'\n6. feladat\n Földrészek amelyekről versenyzők indultak: {földrészekString}')

foldreszek = set()

for item in versenyzok:
    foldreszek.add(item.foldresz)

foldreszekLista = list(foldreszek)
foldreszekLista.sort()
foldreszekString = ', '.join(foldreszekLista)

print(f'\n6. feladat\n Földrészek amelyekről versenyzők indultak: {foldreszekString}')



stat = {}
for item in versenyzok:
    if item.orszag in stat.keys():
        stat[item.orszag] += 1
    else:
        stat[item.orszag] = 1
print('\n7. feladat')
for key,value in stat.items():
    print(f'\t{key}: {value} fő')