from Eredmeny import Eredmeny


eredmenyek :list[Eredmeny] = []

file = open('szar.txt','r', encoding='utf-8')
file.readline()
for sor in file:
    eredmenyek.append(Eredmeny(sor.strip))

file.close()

print(f'3.2 feladat: Futók száma: {len(eredmenyek)}')