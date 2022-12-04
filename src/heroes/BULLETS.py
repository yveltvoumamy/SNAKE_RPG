from random import *


class Missile():

    def __init__(self, coordinate, size, img, facing):
        self.coordinate = coordinate
        self.img = img
        self.size = size
        self.facing = facing
        self.vel = (40 * facing[0], 40 * facing[1])

    def draw(self, sc):
        sc.blit(self.img[randint(0, 1)], (*self.coordinate, self.size, self.size))


class Shot():
    up = (0, -1)
    down = (0, 1)
    right = (1, 0)
    left = (-1, 0)
    right_up = (1, -1)
    right_down = (1, 1)
    left_down = (-1, 1)
    left_up = (-1, -1)

    def eyeball_directions(self):
        directions = [self.right, self.left, self.up, self.down]
        return directions

    def ghost_directions(self):
        directions = [(self.right_up, self.left_down),
                      (self.left_down, self.right_up),
                      (self.up, self.down),
                      (self.right, self.left)
                      ]
        return directions

    def big_worm_directions(self):
        direcctions = [(self.right_up, self.right_down),
                       (self.left_down, self.left_up),
                       (self.right_up, self.left_up),
                       (self.right_down, self.left_down)
                       ]
        return direcctions

    def pumpkin_directions(self):
        directions = [(self.right_up, self.right_down, self.right),
                      (self.left_up, self.left_down, self.left),
                      (self.right_up, self.left_up, self.up),
                      (self.right_down, self.left_down, self.down)]
        return directions

    def man_eater_directions(self):
        eyeball_directions = self.eyeball_directions()
        ghost_directions = self.ghost_directions()
        big_worm_directions = self.big_worm_directions()
        pumpkin_directions = self.pumpkin_directions()
        move_set = [eyeball_directions, ghost_directions, big_worm_directions, pumpkin_directions]
        directions = [[] for i in range(len(move_set))]
        for i in range(len(move_set)):
            directions[i].append([move_set[0][i]])
            for j in range(1, 4):
                directions[i].append(move_set[j][i])
            if i >= 2:
                directions[i].append((self.right, self.left, self.up, self.down))
            else:
                directions[i].append((self.right_up, self.right_down, self.left_up, self.left_down))

        return directions