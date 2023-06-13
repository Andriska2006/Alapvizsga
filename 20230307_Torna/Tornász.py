class Tornász:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.Rajtszám = splitted[0]
        self.Név = splitted[1]
        self.Ország = splitted[2]
        self.Földrész = splitted[3]
        self.Talaj = float(splitted[4].replace(',','.'))
        self.Lólengés = float(splitted[5].replace(',','.'))
        self.Gyűrű = float(splitted[6].replace(',','.'))
        self.Nyújtó = float(splitted[7].replace(',','.'))
        self.Korlát = float(splitted[8].replace(',','.'))
        self.Ugrás = float(splitted[9].replace(',','.'))