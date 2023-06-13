class Repulo:
    def __init__(self, row) -> None:
        # típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv
        # Airbus A300;1972;220-336;3;911;142000;44,84
        splitted = row.split(';')
        self.tipus = splitted[0]
        self.ev = int(splitted[1])
        self.utas = splitted[2]
        self.szemelyzet = splitted[3]
        self.utazosebesseg = int(splitted[4])
        self.felszallotomeg = int(splitted[5])
        self.fesztav = float(splitted[6].replace(',','.'))

        if '-' in self.utas:
            splittedUtas = self.utas.split('-')
            self.utasSzam = int(splittedUtas[1])
        else:
            self.utasSzam = int(self.utas)

        splittedSzemelyzet = self.szemelyzet.split('-')
        self.szemelyzetSzam = splittedSzemelyzet[-1]
