from Ride import Ride

rides : list[Ride] = []

file = open('fuvar.csv','r',encoding='utf-8')
file.readline()
for row in file:
    rides.append(Ride(row.strip()))
file.close()

print(f'3. feladat: {len(rides)} fuvar')

count = 0
sum = 0
for item in rides:
    if item.id == 6185:
        count += 1
        sum += item.price
print(f'4. feladat: {count} fuvar alatt: ${sum}')

stats = {}
for item in rides:
    if item.paymentMethod in stats.keys():
        stats[item.paymentMethod] += 1
    else:
        stats[item.paymentMethod] = 1

print('5. feladat: ')
for key,value in stats.items():
    print(f'\t{key}: {value} fuvar')

sum = 0
for item in rides:
    sum += item.distance
print(f'6. feladat: {sum * 1.6:.2f}km')

longest = rides[0].duration
longestIndex = 0
for index,item in enumerate(rides):
    if item.duration > longest:
        longest = item.duration
        longestIndex = index

print(f'7. feladat: Leghosszabb fuvar:')
print(f'\tFuvar hossza: {longest} másodperc')
print(f'\tTaxi azonosító: {rides[longestIndex].id}')
print(f'\tMegtett távolság: {rides[longestIndex].distance*1.6:.2f} km')
print(f'\tViteldíj: ${rides[longestIndex].price}')

file = open('hibak.txt','w',encoding='utf-8')
for item in rides:
    if item.duration > 0 and item.price > 0 and item.distance == 0:
        file.write(f'{item.id};{item.start};{item.duration};{item.distance};{item.price};{item.tip};{item.paymentMethod}\n')
file.close()