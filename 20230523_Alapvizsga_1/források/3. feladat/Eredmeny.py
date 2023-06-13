class Eredmeny:
    def __init__(self,sor:str) -> None:
        splitted = sor.split(';')
        self.név = splitted[0]
        self.rajtszam = int(splitted[1])
        self.kategoria = splitted[2]
        self.versenyido = splitted[3]
        self.szazalek = int(splitted[4])