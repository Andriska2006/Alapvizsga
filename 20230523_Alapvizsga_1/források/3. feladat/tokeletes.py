def tokeletes_e(szam):
    osszeg = 0
    for i in range(1, szam):
        if szam % i == 0:
            osszeg += i
    if osszeg == szam:
        return True
    return False


print('2. feladat: Tökéletes számok')
print('Kérek két természetes számot:')
tol = int(input('tól = '))
ig = int(input('ig = '))

tokeletesek = []

for i in range(tol, ig+1):
    if tokeletes_e(i) == True:
        tokeletesek.append(i)

print(f'Tökéletes számok {tol} és {ig} között:')
if len(tokeletesek) == 0:
    print('A megadott tartományban nincsen tökéletes szám')
else:
    print('; '.join(map(str,tokeletesek)))