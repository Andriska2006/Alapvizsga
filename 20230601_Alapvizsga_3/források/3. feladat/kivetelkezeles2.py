from math import sqrt

def masodfoku(a,b,c):
    if 4*a*c > b*b:
        raise ValueError('Negatív szám a gyök alatt!!!')
    x1 = (-b + sqrt(b*b - 4*a*c)) / 2*a
    x2 = (-b - sqrt(b*b - 4*a*c)) / 2*a
    return x1, x2

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
try:
    print(f'A másodfokú egyenlet gyökei: {masodfoku(a,b,c)}')
except ValueError as error:
    print(error)