class Utasszallito():
    def __init__(self, sor:str) -> None:
        splitted = sor.split(';')
        self.tipus = splitted[0]
        self.ev = int(splitted[1]) 
        self.utas = splitted[2]
        self.szemelyzet = splitted[3]
        self.utazosebesseg = int(splitted[4])
        self.felszalloTomeg = int(splitted[5])
        self.feszTáv = float(splitted[6].replace(',','.'))

        