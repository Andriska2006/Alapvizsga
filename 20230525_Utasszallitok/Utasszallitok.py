from Repulo import Repulo
import math

repulok : list[Repulo] = []

file = open('utasszallitok.txt','r',encoding='utf-8')
elsosor = file.readline()
for row in file:
    repulok.append(Repulo(row.strip()))
file.close()

print(f'4. feladat: Adatsorok száma: {len(repulok)}')

boeingDarab = 0
for item in repulok:
    if 'Boeing' in item.tipus:
        boeingDarab += 1
print(f'5. feladat: Boeing típusok száma: {boeingDarab}')

legtobbUtas = repulok[0]
for item in repulok:
    if item.utasSzam > legtobbUtas.utasSzam:
        legtobbUtas = item
print('6. feladat: A legtöbb utast szállító repülőgéptípus')
print(f'\tTípus: {legtobbUtas.tipus}')
print(f'\tElső felszállás: {legtobbUtas.ev}')
print(f'\tUtasok száma: {legtobbUtas.utas}')
print(f'\tSzemélyzet: {legtobbUtas.szemelyzet}')
print(f'\tUtazósebesség: {legtobbUtas.utazosebesseg}')

file = open('utasszallitok_new.txt','w', encoding='utf-8')
# file.write('típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n')
file.write(elsosor)
for item in repulok:
    file.write(f'{item.tipus};{item.ev};{item.utasSzam};{item.szemelyzetSzam};{item.utazosebesseg};{round(item.felszallotomeg/1000)};{round(item.fesztav*3.2808)}\n')
file.close()

#Számoljuk meg, hogy melyik évben hányfajta repülőt gyártottak
stat = {}
for item in repulok:
    if item.ev in stat.keys():
        stat[item.ev] += 1
    else:
        stat[item.ev] = 1

print('Statisztika')
#print(stat)
for key,value in stat.items():
    print(f'\t{key}: {value} darab')


# Mach-kalkulátor
torlonyomas = float(input('Tolónyomás: '))
statikusnyomas = float(input('Statikus nyomás: '))

mach = math.sqrt(5 * (math.pow(torlonyomas/statikusnyomas+1,2/7) - 1))
print(f'Mach-érték: {mach}')