
print('1. feladat A háromszög szerkeszthetősége')
print('Kérem a háromsszög oldalait!')

aOldal = float(input('a = '))
bOldal = float(input('b = '))
cOldal = float(input('c = '))

if aOldal + bOldal > cOldal and bOldal + cOldal > aOldal and aOldal + cOldal > bOldal:
    print('A háromszög szerkeszthető!')
else:
    print('A háromszög nem szerkeszthető a megadott adatokkal!')


