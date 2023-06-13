def tokeletes_e(szam):
    osszeg = 0
    for i in range(1, szam):
        if szam % i == 0:
            osszeg += i
    if osszeg == szam:
        return True
    return False

print('2. feladat: Tökéletes számok')
print('Kérek két természetes számot')
bekertTól = int(input('tól = '))
bekertIg =  int(input('ig = '))

tokeletesek = []
for i in range(bekertTól, bekertIg+1):
    if tokeletes_e(i) == True:
        tokeletesek.append(i)
print(f'Tökéletes számok {bekertTól} és {bekertIg} között:')
if len(tokeletesek) == 0:
    print('A megadott tartományban nincs tökéletes szám')
else:
    print(';'.join(map(str,tokeletesek)))
