import random


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


class Ship:
    def __init__(self, coordx, coordy, size,
                 direction=0):  # direction:1-horizontal right 2-horizontal left 3- vertical up 4-vertical down
        self.coordx = coordx
        self.coordy = coordy
        self.size = size
        self.direction = direction


def winner(poly):
    for i in range(6):
        if '▪' in poly[i]:
            return False
    return True


def step(coordX, coordY, poly):
    f = 0
    try:
        if poly[coordY][coordX] == '▪':
            poly[coordY][coordX] = 'X'
            print('Вы попали, следующий ход')
            f = 1
        elif poly[coordY][coordX] == 'T' or poly[coordY][coordX] == 'X':
            print('Выберите другую клетку для атаку, сюда уже стреляли')
            f = 1
        elif poly[coordY][coordX] == 'o':
            poly[coordY][coordX] = 'T'
            print('Вы промахнулись')
            f = 0
    except IndexError:
        print('Введите координаты меньше, вы вышли за пределы поля')
        f = 1
    finally:
        return f


def game(poly_p, poly_c, step_game):
    while True:
        if step_game == 1:
            coordX = int(input('Введите координату Х')) - 1
            coordY = int(input('Введите координату Y')) - 1
            if step(coordX, coordY, poly_c) != 1:
                step_game = 0
        else:

            coordX = random.randint(1, 6) - 1
            coordY = random.randint(1, 6) - 1

            if step(coordX, coordY, poly_p) != 1:
                step_game = 1
        yield step_game


def Check_poly_on_space(poly):
    f = 1
    for i in range(6):
        for j in range(6):
            if poly.ship_correct(Ship(i + 1, j + 1, 1)):
                f = 0
    if f == 1:
        for i in range(6):
            for j in range(6):
                poly.poly[i][j] = 'o'
    return f


def start_game(polygon_player, polygon_comp):
    print(
        "Добро пожаловать в игру Морской бой.\nПравила:\n1)У вас есть 7 кораблей(один трехпалубный, два двухпалубных и 4 однопалубных), на поле 6 на 6 клеток.\n2)Корабли нужно расставлять на расстоянии не менее одной клетки друг от друга.\n3)Победит тот кто первый разрушит все корабли.\n")
    c3 = 1
    c2 = 2
    c1 = 4
    print('Приступим к расстановке кораблей')
    while True and (c1 != 0 or c2 != 0 or c3 != 0):
        try:
            if c1 > 0 and c2 == 0 and c3 == 0 and Check_poly_on_space(polygon_player):
                c3 = 1
                c2 = 2
                c1 = 4
                print('Вам надо заполнить поле заного, корабли не поместились')
            if c3 > 0:
                coordx = int(input('Введите координату х 3палубного корабля 1-6'))
                coordy = int(input('Введите координату у 3палубного корабля 1-6'))
                if 1 <= coordx <= 6 and 1 <= coordy <= 6:
                    direction = int(input(
                        'Введите направление 3палубного корабля: 1-по горизонтали вправо\n2- по горизонтали влево\n3- по вертикали вверх\n4- по вертикали вниз\n'))
                    if 1 <= direction <= 4:
                        if polygon_player.add_ship(Ship(coordx, coordy, 3, direction)):
                            c3 -= 1
                else:
                    continue
            elif c2 > 0:
                coordx = int(input('Введите координату х 2палубного корабля 1-6'))
                coordy = int(input('Введите координату у 2палубного корабля 1-6'))
                if 1 <= coordx <= 6 and 1 <= coordy <= 6:
                    direction = int(input(
                        'Введите направление 3палубного корабля: 1-по горизонтали вправо\n2- по горизонтали влево\n3- по вертикали вверх\n4- по вертикали вниз\n'))
                    if 1 <= direction <= 4:
                        if polygon_player.add_ship(Ship(coordx, coordy, 2, direction)):
                            c2 -= 1
                else:
                    continue
            elif c1 > 0:
                coordx = int(input('Введите координату х 1палубного корабля 1-6'))
                coordy = int(input('Введите координату у 1палубного корабля 1-6'))
                if 1 <= coordx <= 6 and 1 <= coordy <= 6:
                    if polygon_player.add_ship(Ship(coordx, coordy, 1)):
                        c1 -= 1
                else:
                    continue
        except ValueError:
            continue
        print(polygon_player)
    c3 = 1
    c2 = 2
    c1 = 4
    while True and (c1 > 0 or c2 > 0 or c3 > 0):
        if c1 > 0 and c2 == 0 and c3 == 0 and Check_poly_on_space(polygon_comp):
            c3 = 1
            c2 = 2
            c1 = 4
            print('Компьютер заполняет поле заного, корабли не поместились')
        if c3 > 0:
            coordx = random.randint(1, 6)
            coordy = random.randint(1, 6)
            direction = random.randint(1, 4)
            if polygon_comp.add_ship(Ship(coordx, coordy, 3, direction)):
                c3 -= 1
        elif c2 > 0:
            coordx = random.randint(1, 6)
            coordy = random.randint(1, 6)
            direction = random.randint(1, 4)
            if polygon_comp.add_ship(Ship(coordx, coordy, 2, direction)):
                c2 -= 1
        elif c1 > 0:
            coordx = random.randint(1, 6)
            coordy = random.randint(1, 6)
            if polygon_comp.add_ship(Ship(coordx, coordy, 1)):
                c1 -= 1
        print(polygon_comp)


polyc = []
polyp = []
polygon_player = Polygon(polyp)
polygon_computer = Polygon(polyc)
start_game(polygon_player, polygon_computer)
step_game = 1
print('Корабли на местах, начнем бой!')
print('Введите координаты поля противника, куда хотите стрелять:')
while not(winner(polygon_player.poly)) and not(winner(polygon_computer.poly)):
    try:
        step_game = next(game(polygon_player.poly, polygon_computer.poly, step_game))
        print(polygon_player)
        print(polygon_computer)
    except ValueError:
        print('Вводите числа от 1 до 6')
if winner(polygon_computer.poly):
    print('Поздравляю вы выиграли!')
else:
    print('Вы проиграли. Не расстраивайтесь, повезет в следующий раз!')
