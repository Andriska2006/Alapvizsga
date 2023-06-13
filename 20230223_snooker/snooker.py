from Player import Player

players : list[Player] = []

file = open('snooker.txt','r',encoding='utf-8')
file.readline()
for row in file:
    players.append(Player(row.strip()))
file.close()

print(f'3. feladat: A világranglistán {len(players)} versenyző szerepel.')

sum = 0
for item in players:
    sum += item.prize
print(f'4. feladat: A versenyzők átlagosan {sum / len(players):.2f} fontot kerestek.')

max = -99999
maxIndex = -1
for index,item in enumerate(players):
    if item.country == 'Kína' and max < item.prize:
        max = item.prize
        maxIndex = index
print('5. feladat: A legjobban kereső kínai versenyző: ')
print(f'\tHelyezés: {players[maxIndex].position}')
print(f'\tNév: {players[maxIndex].name}')
print(f'\tOrszág: {players[maxIndex].country}')
print(f'\tNyeremény: {players[maxIndex].prize * 380:,} Ft')

vanNorveg = False
for item in players:
    if item.country == 'Norvégia':
        vanNorveg = True
        break
if vanNorveg:
    print('6. feladat: A versenyzők között van norvég versenyző.')
else:
    print('6. feladat: A versenyzők között nincs norvég versenyző.')

for item in players:
    if item.country == 'Skócia':
        print('6+1. feladat: A versenyzők között van skót versenyző.')
        break
else:
    print('6+1. feladat: A versenyzők között nincs skót versenyző.')


stats = {}
for item in players:
    if item.country in stats.keys():
        stats[item.country] += 1
    else:
        stats[item.country] = 1

print('7. feladat: Statisztika')
# for item in stats.items():
#     print(f'\t{item[0]} - {item[1]}')

for key,value in sorted(stats.items()):
    print(f'\t{key} - {value}')