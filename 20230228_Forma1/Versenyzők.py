from Pilot import *

pilots : list[Pilot] = []

file = open('pilotak.csv', 'r', encoding='utf-8')
file.readline()
for row in file:
    pilots.append(Pilot(row.strip()))
file.close

print(f'3. feladat: {len(pilots)}')

print(f'4. feladat: {pilots[-1].name}')

print('5. feladat: ')

for item in pilots:
    if item.year < 1901:
        print(f'\t{item.name} ({item.birthday})')

min = 99999999
minIndex = -1
for i, item in enumerate(pilots):
    if item.position != '':
        startNumber = int(item.position)
        if startNumber < min:
            min = startNumber
            minIndex = i


print(f'6. feladat: {pilots[minIndex].country}')
       

stat = {}
for item in pilots:
    if item.position in stat.keys():
        stat[item.position] += 1
    else:
        stat[item.position] = 1

print('7. feladat: ', end='')
first = True
for key,value in stat.items():
    if key != '' and value > 1:
        if first != True:
             print(f', {key}', end=' ')
        else:
            print(f'{key}', end='')
            first = False