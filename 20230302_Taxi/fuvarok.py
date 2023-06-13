from Fuvar import *

fuvarok : list[Fuvar] = []

file = open('fuvar.csv', 'r', encoding='utf-8')
file.readline()
for sor in file:
    fuvarok.append(Fuvar(sor.strip()))
file.close()

print(f'3. feladat: {len(fuvarok)} fuvar')

count = 0
sum = 0
for item in fuvarok:
    if item.id == 6185:
       count += 1
       sum += item.viteldij
print(f'4. feladat: {count} fuvar alatt: ${sum}') 
        
print('5. feladat:')

stats = {}
for item in fuvarok:
    if item.fizetesMod in stats.keys():
        stats[item.fizetesMod] += 1
    else:
        stats[item.fizetesMod] = 1

for key,value in stats.items():
    print(f'\t{key}: {value} fuvar')

sum = 0
for item in fuvarok:
    sum += item.tavolsag
    km = sum * 1.6

print(f'6. feladat: {round(km,2)}km')

max = 0
maxIndex = 0
for i, item in enumerate(fuvarok):
    if item.idotartam > max:
        max = item.idotartam
        maxIndex = i

print('7. feladat: Leghosszabb fuvar:')
print(f'\tFuvar hossza: {fuvarok[maxIndex].idotartam} másodperc')
print(f'\tTaxi azonositó: {fuvarok[maxIndex].id}')
print(f'\tMegtett távolság: {fuvarok[maxIndex].tavolsag*1.6:.2f} km')
print(f'\tViteldíj: ${fuvarok[maxIndex].viteldij}')

file = open('hibak.txt', 'w', encoding='utf-8')
for item in fuvarok:
    if item.idotartam > 0 and item.viteldij > 0 and item.tavolsag == 0:
        file.write(f'{item.id};{item.indulasiIdopont};{item.idotartam};{item.viteldij};{item.borravalo};{item.fizetesMod}\n')
file.close()