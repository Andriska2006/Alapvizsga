def maganhangzokSzama(nap):
    maganhangzok = 'aáeéiíoóöőuúüű'
    darab = 0
    for item in nap:
        if item in maganhangzok:
            darab += 1
    return darab


napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

maxNap = napok[0] 
for item in napok:
    if maganhangzokSzama(item)>maganhangzokSzama(maxNap):
        maxNap = item

print(f'A legtöbb magánhangző a {maxNap}-ben van.')