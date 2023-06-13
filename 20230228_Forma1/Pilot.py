class Pilot:
    def __init__(self, row:str) -> None:
        # név;születési_dátum;nemzetiség;rajtszám
        splitted = row.split(';')
        self.name = splitted[0]
        self.birthDate = splitted[1]
        self.nationality = splitted[2]
        self.startNumber = splitted[3]

        # 1991.03.22
        splittedYear = self.birthDate.split('.')
        self.year = int(splittedYear[0])