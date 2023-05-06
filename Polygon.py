class Ship:
    def __init__(self, coordx, coordy, size,
                 direction=0):  # direction:1-horizontal right 2-horizontal left 3- vertical up 4-vertical down
        self.coordx = coordx
        self.coordy = coordy
        self.size = size
        self.direction = direction
class Polygon:
    def __init__(self, poly):
        for i in range(6):
            poly.append(['o'] * 6)
        self.poly = poly

    def __getitem__(self, item):
        return self.poly

    def __str__(self):
        s = ' |1|2|3|4|5|6|\n'
        for i in range(6):
            s += str(i + 1)
            for j in range(6):
                s += f'|{self.poly[i][j]}'
            s += '|\n'
        return s

    def add_ship(self, ship):
        if self.ship_correct(ship):
            if ship.direction == 1:
                for i in range(ship.size):
                    self.poly[ship.coordy - 1][ship.coordx - 1 + i] = '▪'
            elif ship.direction == 2:
                for i in range(ship.size):
                    self.poly[ship.coordy - 1][ship.coordx - 1 - i] = '▪'
            elif ship.direction == 3:
                for i in range(ship.size):
                    self.poly[ship.coordy - 1 - i][ship.coordx - 1] = '▪'
            elif ship.direction == 4:
                for i in range(ship.size):
                    self.poly[ship.coordy - 1 + i][ship.coordx - 1] = '▪'
            elif ship.direction == 0:
                self.poly[ship.coordy - 1][ship.coordx - 1] = '▪'
            return True
        else:
            return False

    #Проверка координат вокруг корабля, то что можно ставить корабль в указанные координаты.
    def coord_correct(self, ship):
        f = True
        if ship.direction == 1:
            for i in range(ship.coordx - 2, ship.coordx + ship.size):
                for j in range(ship.coordy - 2, ship.coordy + 1):
                    if 1 <= i + 1 <= 6 and 1 <= j + 1 <= 6:
                        if self.poly[j][i] == '▪':
                            f = False
                            print(1)
        elif ship.direction == 2:
            for i in range(ship.coordx - ship.size - 1, ship.coordx + 1):
                for j in range(ship.coordy - 2, ship.coordy + 1):
                    if 1 <= i + 1 <= 6 and 1 <= j + 1 <= 6:
                        if self.poly[j][i] == '▪':
                            f = False
                            print(2)
        elif ship.direction == 3:
            for i in range(ship.coordx - 2, ship.coordx + 1):
                for j in range(ship.coordy - ship.size - 1, ship.coordy + 1):
                    if 1 <= i + 1 <= 6 and 1 <= j + 1 <= 6:
                        if self.poly[j][i] == '▪':
                            f = False
                            print(3)
        elif ship.direction == 4:
            for i in range(ship.coordx - 2, ship.coordx + 1):
                for j in range(ship.coordy - 2, ship.coordy + ship.size + 1):
                    if 1 <= i + 1 <= 6 and 1 <= j + 1 <= 6:
                        if self.poly[j][i] == '▪':
                            f = False
                            print(4)
        elif ship.direction == 0:
            for i in range(ship.coordx - 2, ship.coordx + 1):
                for j in range(ship.coordy - 2, ship.coordy + 1):
                    if 1 <= i + 1 <= 6 and 1 <= j + 1 <= 6:
                        if self.poly[j][i] == '▪':
                            f = False
                            print(5)
        else:
            f = False
        return f

    #Проверка координат, для установки корабля
    def ship_correct(self, ship):
        f = False
        if self.coord_correct(ship):
            if ship.direction == 1:
                if 1 <= ship.coordx + ship.size - 1 <= 6 and 1 <= ship.coordy <= 6:
                    f = True
            elif ship.direction == 2:
                if 1 <= ship.coordx - ship.size + 1 <= 6 and 1 <= ship.coordy <= 6:
                    f = True
            elif ship.direction == 3:
                if 1 <= ship.coordx <= 6 and 1 <= ship.coordy - ship.size + 1 <= 6:
                    f = True
            elif ship.direction == 4:
                if 1 <= ship.coordx <= 6 and 1 <= ship.coordy + ship.size - 1 <= 6:
                    f = True
            elif ship.direction == 0:
                f = True
            else:
                f = False
        return f