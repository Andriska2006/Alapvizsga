class Fuvar:
    def __init__(self,sor:str) -> None:
        splitted = sor.split(';')
        self.id = int(splitted[0])
        self.indulasiIdopont = splitted[1]
        self.idotartam = int(splitted[2])
        self.tavolsag = float(splitted[3].replace(',', '.'))
        self.viteldij = float(splitted[4].replace(',', '.'))
        self.borravalo = float(splitted[5].replace(',', '.'))
        self.fizetesMod = splitted[6]