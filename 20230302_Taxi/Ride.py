class Ride:
    # taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.id = int(splitted[0])
        self.start = splitted[1]
        self.duration = int(splitted[2])
        self.distance = float(splitted[3].replace(',', '.'))
        self.price = float(splitted[4].replace(',', '.'))
        self.tip = float(splitted[5].replace(',', '.'))
        self.paymentMethod = splitted[6]
