from Tornász import Tornász

tornászok : list[Tornász] = []

with open('torna.csv','r',encoding='utf-8') as file:
    file.readline()
    for row in file:
        tornászok.append(Tornász(row.strip()))
print(f'2. feladat\nÖsszesen {len(tornászok)} versenyző indult a versenyen')

maxÉrték = tornászok[0].Korlát
maxElem = tornászok[0]
for item in tornászok:
    if item.Korlát > maxÉrték:
        maxÉrték = item.Korlát
        maxElem = item
print(f'3.feladat\nKorláton {maxElem.Név} szerzte meg az aranyérmet.')

rajtszám = input('4. feladat\nKérem a versenyző rajtszámát: ')
for item in tornászok:
    if item.Rajtszám == rajtszám:
        print(f'A {rajtszám} rajtszámú versenyző gyűrűn elért eredménye: {item.Gyűrű} pont.')
        break
else:
    print('Nincs ilyen versenyző.')

print(f'5. feladat\nLólengésben nem jutottak döntőbe:')
for item in tornászok:
    if item.Lólengés < 14.5:
        print(f'\t{item.Név}')

földrészek : list[str] = []
for item in tornászok:
    if item.Földrész not in földrészek:
        földrészek.append(item.Földrész)
földrészek.sort()
földrészekString = ', '.join(földrészek)
print(f'6. feladat\nFöldrészek amelyekről versenyzők indultak: {földrészekString}')

statisztika = {}
for item in tornászok:
    if item.Ország in statisztika.keys():
        statisztika[item.Ország] += 1
    else:
        statisztika[item.Ország] = 1
print('7. feladat')
for key,value in statisztika.items():
    print(f'\t{key}: {value} fő')