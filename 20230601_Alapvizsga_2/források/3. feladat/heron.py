import math

print('1. feladat: Háromszög kerülete, területe')
print('Kérem a háromszög oldalait')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
print(f'K = {a + b + c}')
s = (a + b + c) / 2
t = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f'T = {t}')