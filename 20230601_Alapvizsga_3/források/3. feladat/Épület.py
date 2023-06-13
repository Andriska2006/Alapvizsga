class Épület:
    def __init__(self, row) -> None:
        splitted = row.strip().split(';')
        
        self.név = splitted[0]
        self.város = splitted[1]
        self.ország = splitted[2]
        self.magasság = float(splitted[3].replace(',','.'))
        self.emelet = int(splitted[4])
        self.épül = int(splitted[5])
        