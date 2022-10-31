from constants import *


class Map():
    def __init__(self):
        self.width = MAP_SIZE["width"]
        self.height = MAP_SIZE["height"]
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    def upload_map(self, map: list):
        self.map = map

    def get_neighbours(self, x, y) -> list:
        res = []
        for delta_x in range(-1, 2, 1):
            for delta_y in range(-1, 2, 1):
                if delta_x != 0 or delta_y != 0:
                    coord = (x + delta_x, y + delta_y)
                    if (0 <= coord[0] <= self.width - 1 and 0 <= coord[1] <= self.height - 1):
                        res.append(coord)
        return res

    def get_neighbourhood(self, x, y):
        res = {key: [0, []] for key in TYPES_OF_CELLS}
        for neighbour in self.get_neighbours(x, y):
            res[self.map[neighbour[1]][neighbour[0]]][0] += 1
            res[self.map[neighbour[1]][neighbour[0]]][1].append((x, y))
        return res

    def analyse(self) -> dict:
        should_be_open = set()
        should_be_flag = set()
        for deep in range(4):
            for x in range(self.width):
                for y in range(self.height):
                    neighbourhood = self.get_neighbourhood(x, y)
                    if self.map[y][x] not in 'FOC':
                        if int(self.map[y][x]) - neighbourhood['F'][0] == 0 and neighbourhood['C'][0] != 0:
                            for cell in self.get_neighbours(x, y):
                                if self.map[cell[1]][cell[0]] == 'C':
                                    self.map[cell[1]][cell[0]] = 'O'
                                    should_be_open.add(cell)
                        if int(self.map[y][x]) - neighbourhood['F'][0] == neighbourhood['C'][0] and neighbourhood['C'][0]:
                            for cell in self.get_neighbours(x, y):
                                if self.map[cell[1]][cell[0]] == 'C':
                                    self.map[cell[1]][cell[0]] = 'F'
                                    should_be_flag.add(cell)
        return {
            'open': should_be_open,
            'flag': should_be_flag
        }

    def __str__(self) -> str:
        res = ""
        for row in self.map:
            for el in row:
                res += str(el) + " "
            res += "\n"
        return res


if __name__ == '__main__':
    map = Map()
    map.upload_map([['O' for x in range(18)] for y in range(14)])
    map.analyse()
