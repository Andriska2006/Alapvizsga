class Player:
    def __init__(self, row) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.category = splitted[1]
        self.team = splitted[2]
        self.points = []
        for item in splitted[3:]:
            self.points.append(int(item))
    
    def totalPoints(self):
        self.points.sort()
        sum = 0
        for item in self.points[2:]:
            sum += item
        
        return sum
