from Pilot import Pilot

pilots : list[Pilot] = []

file = open('pilotak.csv', 'r', encoding='utf-8')
file.readline()
for row in file:
    # rossz esetek
    # pilots.append(Pilot)
    # pilots.append(row)
    pilots.append(Pilot(row.strip()))
file.close()

print(f'3. feladat: {len(pilots)}')

# pilots[len(pilots)-1]
print(f'4. feladat: {pilots[-1].name}')

print('5. feladat:')
for item in pilots:
    if item.year < 1901:
        print(f'\t{item.name} ({item.birthDate})')

min = 999999
minIndex = -1
for index,item in enumerate(pilots):
    if item.startNumber != '':
        startNumber = int(item.startNumber)
        if startNumber < min:
            min = startNumber
            minIndex = index

print(f'6. feladat: {pilots[minIndex].name} - {pilots[minIndex].nationality}')

stat = {}
for item in pilots:
    if item.startNumber in stat.keys():
        stat[item.startNumber] += 1
    else:
        stat[item.startNumber] = 1

print('7. feladat: ', end='')
first = True
for key,value in stat.items():
    if key != '' and value > 1:
        if first != True:
            print(f', {key}', end='')
        else:
            print(f'{key}', end='')
            first = False
