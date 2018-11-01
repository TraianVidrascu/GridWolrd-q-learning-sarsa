from random import random, randint

from main.gridworld import GridWorld


class Learning:
    def __init__(self):
        self.epsilon = 0.9
        self.alpha = 0.3
        self.lam = 1.0
        self.q_values = [[[0.0]]]
        self.world = GridWorld()
        self.init_q_values()

    def init_q_values(self):
        self.q_values = [[[0, 0, 0, 0] for y in range(0, 8)] for x in range(0, 8)]

    def chose_action(self, x, y):
        action = 0
        best = self.q_values[x][y][0]
        if random() < self.epsilon:
            for i in range(0, 4):
                if self.q_values[x][y][i] > best:
                    action = i
                    best = self.q_values[x][y][i]
        else:
            action = randint(0, 3)

        return action

    def get_max(self, x, y):
        maxi = self.q_values[x][y][0]
        for i in range(0, 4):
            if self.q_values[x][y][i] > maxi:
                maxi = self.q_values[x][y][i]
        return maxi

    def is_terminal(self, x, y):
        if x == 7 and y == 7:
            return True
        if x == 5 and y == 4:
            return True
        return False

    def q_learning(self):
        self.init_q_values()
        for episode in range(0, 10000):
            x, y = self.world.init_state()
            while True:
                a = self.chose_action(x, y)
                r, n_x, n_y = self.world.basic_moves(x, y, a)
                self.q_values[x][y][a] = self.q_values[x][y][a] + self.alpha * (
                        r + self.lam * self.get_max(n_x, n_y) - self.q_values[x][y][a])
                x = n_x
                y = n_y
                if self.is_terminal(x, y):
                    break

    def sarsa(self):
        self.init_q_values()
        for episode in range(0, 10000):
            x, y = self.world.init_state()
            while True:
                a = self.chose_action(x, y)
                r, n_x, n_y = self.world.basic_moves(x, y, a)
                a_prime = self.chose_action(n_x, n_y)
                self.q_values[x][y][a] = self.q_values[x][y][a] + self.alpha * (
                        r + self.lam * self.q_values[n_x][n_y][a_prime] - self.q_values[x][y][a])
                x = n_x
                y = n_y
                if self.is_terminal(x, y):
                    break

    def print_matrix(self):
        for i in range(0, len(self.q_values)):
            line = ""
            for j in range(0, len(self.q_values[i])):
                best = self.q_values[i][j][0]
                for k in range(0, 4):
                    if self.q_values[i][j][k] > best:
                        best = self.q_values[i][j][k]
                line += str(round(best, 1))+" "
            print line
        print "\n"

    def print_policy(self):
        for i in range(0, 8):
            line = ""
            for j in range(0, 8):
                action = 0
                best = self.q_values[i][j][0]
                for k in range(0, 4):
                    if self.q_values[i][j][k] > best:
                        best = self.q_values[i][j][k]
                        action = k
                if best == 0:
                    line += "X "
                elif action == GridWorld.NORTH:
                    line += "N "
                elif action == GridWorld.EAST:
                    line += "E "
                elif action == GridWorld.SOUTH:
                    line += "S "
                elif action == GridWorld.WEST:
                    line += "W "
            print line


l = Learning()
l.sarsa()
l.print_policy()
l.print_matrix()
