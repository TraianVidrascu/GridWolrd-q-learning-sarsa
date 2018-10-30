from random import randint


class GridWorld:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    ACTIONS = [NORTH, EAST, SOUTH, WEST]

    def __init__(self):
        self.size = -1
        self.world = [[]]
        self.init()

    def init(self):
        self.size = 8
        self.world = [[-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, 0, 0, 0, 0, -1, -1],
                      [-1, -1, -1, -1, -1, 0, -1, -1], [-1, -1, -1, -1, -1, 0, -1, -1], [-1, -1, -1, -1, -1, 0, -1, -1],
                      [-1, -1, -1, -1, -20, -1, -1, -1], [-1, 0, 0, 0, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, 10]]

    def basic_moves(self, x, y, action):
        if action == GridWorld.NORTH:
            if x - 1 >= 0 and self.world[x - 1][y] != 0:
                x -= 1

        elif action == GridWorld.EAST:
            if y + 1 < self.size and self.world[x][y + 1] != 0:
                y += 1

        elif action == GridWorld.SOUTH:
            if x + 1 < self.size and self.world[x + 1][y] != 0:
                x += 1

        elif action == GridWorld.WEST and self.world[x][y - 1] != 0:
            if y - 1 >= 0:
                y -= 1

        return self.world[x][y], x, y

    def init_state(self):
        while True:
            x = randint(0, 7)
            y = randint(0, 7)
            if self.world[x][y] == -1:
                return x, y

