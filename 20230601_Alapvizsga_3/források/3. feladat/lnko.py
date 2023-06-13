print('LNKO kivonásos algoritmussal')
a = int(input('a = '))
b = int(input('b = '))

if a > b:
    nagyobb = a
    kisebb = b
else:
    nagyobb = b
    kisebb = a

while nagyobb != kisebb:
    nagyobb = nagyobb - kisebb
    if nagyobb < kisebb:
        temp = nagyobb
        nagyobb = kisebb
        kisebb = temp

print(f'LNKO({a},{b}) = {nagyobb}')