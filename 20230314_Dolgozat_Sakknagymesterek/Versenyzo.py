class Versenyzo:
    def __init__(self,sor:str) -> None:
        splitted = sor.split(';')
        # azonosító;név;ország;neme;élő-pontszám;születésiÉv
        self.azonosito = int(splitted[0])
        self.nev = splitted[1]
        self.orszag = splitted[2]
        self.neme = splitted[3]
        self.pontszam = int(splitted[4])
        self.szuletesiEv = int(splitted[5]) 

    def szuperNagyMester(self):
        nagymesteriRang = []
        mesterek = 0
        if self.neme == 'F' and self.pontszam > 2700 or self.neme == 'N' and self.pontszam > 2500:
            return nagymesteriRang.append(mesterek)


