try:
    raise NameError('Name hiba')
    szam = int(input('szam = '))

except ValueError as error:
    # print(error)
    print('Nem megfelelő szám adat!')
except NameError:
    print('Elfogtam a name errort.')
print('A program tovább megy')