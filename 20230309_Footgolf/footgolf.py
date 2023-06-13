from Player import Player

players : list[Player] = []

file = open('fob2016.txt','r',encoding='utf-8')
for row in file:
    players.append(Player(row.strip()))
file.close()

print(f'3. feladat: Játékosok száma: {len(players)}')

countWomen = 0
for item in players:
    if item.category == 'Noi':
        countWomen += 1
print(f'4. feladat: A női versenyzők aránya: {countWomen/len(players)*100:.2f}%')

