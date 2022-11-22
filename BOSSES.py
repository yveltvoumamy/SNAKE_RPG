from pygame import *
from random import *
import pygame.math


class snaryad():

    def __init__(self, coordinate, size, img, facing):
        self.coordinate = coordinate
        self.img = img
        self.size = size
        self.facing = facing
        self.vel = (40 * facing[0], 40 * facing[1])

    def draw(self, sc):
        sc.blit(self.img[randint(0, 1)], (*self.coordinate, self.size, self.size))


class Eyeball():
    delay = 6
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load(f'Eyeball/eyeball_right 80x60/eyeball_right{i}.png'.format(i)) for i in range(1, 7)]

        self.left = [pygame.image.load(f'Eyeball/eyeball_left 80x60/eyeball_left{i}.png'.format(i)) for i in range(1, 7)]


        self.up = [pygame.image.load(f'Eyeball/eyeball_up 80x60/eyeball_up{i}.png'.format(i)) for i in range(1, 7)]

        self.down = [pygame.image.load(f'Eyeball/eyeball_down 80x60/eyeball_down{i}.png'.format(i)) for i in range(1, 7)]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = [[pygame.image.load('Eyeball/bullet 80x60/bullet_right.png') for i in range(2)],

                       [pygame.image.load('Eyeball/bullet 80x60/bullet_left.png') for i in range(2)],

                       [pygame.image.load('Eyeball/bullet 80x60/bullet_up.png') for i in range(2)],

                        [pygame.image.load('Eyeball/bullet 80x60/bullet_down.png') for i in range(2)]]

        self.direcctions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        self.choose_action()

    def choose_action(self):
        self.animcount = 0
        r = randint(0, 3)
        self.current_action = self.actions[r]

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                   self.bullet[self.actions.index(self.current_action)],
                                   self.direcctions[self.actions.index(self.current_action)]))
            self.choose_action()
        self.animcount += 1
        x = 0
        for i in range(self.lifes):
            pygame.draw.rect(self.sc, pygame.Color('red'), (100 + x, 980, 40, 10))
            x += 40

    def move_from(self, snake):
        if not randint(0, 10):
            self.coordinate = Vector2(randrange(
                self.coordinate[0] - self.width if self.coordinate[0] - self.width > 0 else self.coordinate[0],
                self.coordinate[0] + self.width * 2 if self.coordinate[0] + self.width < self.RES else self.RES, self.width),
                randrange(self.coordinate[1] - self.width if self.coordinate[1] - self.width > 0 else self.coordinate[1],
                          self.coordinate[1] + self.width * 2 if self.coordinate[1] + self.width < self.RES else self.RES,
                          self.width))
            while list(x for x in self.coordinate) in list(list(y * self.width for y in x) for x in snake.body)\
                    or self.coordinate.x < 0 or self.coordinate.x > self.RES or self.coordinate.y < 0 or \
                    self.coordinate.y > self.RES:
                self.coordinate = Vector2(randrange(
                    self.coordinate[0] - self.width if self.coordinate[0] - self.width > 0 else self.coordinate[0],
                    self.coordinate[0] + self.width * 2 if self.coordinate[0] + self.width < self.RES else self.RES,
                    self.width), \
                    randrange(self.coordinate[1] - self.width if self.coordinate[1] - self.width > 0 else self.coordinate[1],
                              self.coordinate[1] + self.width * 2 if self.coordinate[1] + self.width < self.RES else self.RES,
                              self.width))


class Ghost(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load(f'ghost/ghost_right/ghost_right{i}.png'.format(i)) for i in range(1, 7)]

        self.left = [pygame.image.load(f'ghost/ghost_left/ghost_left{i}.png'.format(i)) for i in range(1, 7)]

        self.up = [pygame.image.load(f'ghost/ghost_up/ghost_up{i}.png'.format(i)) for i in range(1, 7)]

        self.down = [pygame.image.load(f'ghost/ghost_down/ghost_down{i}.png'.format(i)) for i in range(1, 7)]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = [([pygame.image.load(f'fireball/fireball_diag{i}/fireball_right_up{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_down{i}.png'.format(i)) for i in range(1, 3)]),

                       ([pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_up{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_diag{i}/fireball_right_down{i}.png'.format(i)) for i in range(1, 3)]),

                       ([pygame.image.load(f'fireball/fireball_straight{i}/fireball_up{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_straight{i}/fireball_down{i}.png'.format(i)) for i in range(1, 3)]),

                       ([pygame.image.load(f'fireball/fireball_straight{i}/fireball_right{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_straight{i}/fireball_left{i}.png'.format(i)) for i in range(1, 3)])]

        self.direcctions = [((1, -1), (-1, 1)), ((-1, -1), (1, 1)), ((0, -1), (0, 1)), ((1, 0), (-1, 0))]
        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                   self.bullet[self.actions.index(self.current_action)][0],
                                   self.direcctions[self.actions.index(self.current_action)][0]))
            bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                   self.bullet[self.actions.index(self.current_action)][1],
                                   self.direcctions[self.actions.index(self.current_action)][1]))
            self.choose_action()
        self.animcount += 1
        x = 0
        for i in range(self.lifes):
            pygame.draw.rect(self.sc, pygame.Color('red'), (100 + x, 980, 40, 10))
            x += 40



class BigWorm(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load(f'big_worm/big_worm_right/worm_right{i}.png'.format(i)) for i in range(1, 7)]

        self.left = [pygame.image.load(f'big_worm/big_worm_left/worm_left{i}.png'.format(i)) for i in range(1, 7)]

        self.up = [pygame.image.load(f'big_worm/big_worm_up/worm_up{i}.png'.format(i)) for i in range(1, 7)]

        self.down = [pygame.image.load(f'big_worm/big_worm_down/worm_down{i}.png'.format(i)) for i in range(1, 7)]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = [((pygame.image.load('fireball/fireball_diag1/fireball_right_up1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_right_up2.png')),
                        (pygame.image.load('fireball/fireball_diag1/fireball_right_down1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_right_down2.png')),
                        ),
                       ((pygame.image.load('fireball/fireball_diag1/fireball_left_up1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_left_up2.png')),
                        (pygame.image.load('fireball/fireball_diag1/fireball_left_down1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_left_down2.png')),
                        ),
                       ((pygame.image.load('fireball/fireball_diag1/fireball_right_up1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_right_up2.png')),
                        (pygame.image.load('fireball/fireball_diag1/fireball_left_up1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_left_up2.png')),
                        ),
                       ((pygame.image.load('fireball/fireball_diag1/fireball_right_down1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_right_down2.png')),
                        (pygame.image.load('fireball/fireball_diag1/fireball_left_down1.png'),
                         pygame.image.load('fireball/fireball_diag2/fireball_left_down2.png')),
                        )
                       ]

        self.direcctions = [((1, -1), (1, 1)), ((-1, -1), (-1, 1)), ((1, -1), (-1, -1)), ((1, 1), (-1, 1))]
        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            for i in range(len(self.bullet[self.actions.index(self.current_action)])):
                bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                       self.bullet[self.actions.index(self.current_action)][i],
                                       self.direcctions[self.actions.index(self.current_action)][i]))
            self.choose_action()
        self.animcount += 1
        x = 0
        for i in range(self.lifes):
            pygame.draw.rect(self.sc, pygame.Color('red'), (100 + x, 980, 40, 10))
            x += 40


class Pumpking(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load(f'pumpkin/pumpkin_right/pumpkin_right{i}.png'.format(i)) for i in range(1, 7)]

        self.left = [pygame.image.load(f'pumpkin/pumpkin_left/pumpkin_left{i}.png'.format(i)) for i in range(1, 7)]

        self.up = [pygame.image.load(f'pumpkin/pumpkin_up/pumpkin_up{i}.png'.format(i)) for i in range(1, 7)]

        self.down = [pygame.image.load(f'pumpkin/pumpkin_down/pumpkin_down{i}.png'.format(i)) for i in range(1, 7)]

        self.actions = [self.right, self.left, self.up, self.down]


        self.bullet = [([pygame.image.load(f'fireball/fireball_diag{i}/fireball_right_up{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_down{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_straight{i}/fireball_right{i}.png'.format(i)) for i in range(1, 3)]
                        ),
                       ([pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_up{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_down{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_straight{i}/fireball_left{i}.png'.format(i)) for i in range(1, 3)]
                        ),
                       ([pygame.image.load(f'fireball/fireball_diag{i}/fireball_right_up{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_up{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_straight{i}/fireball_up{i}.png'.format(i)) for i in range(1, 3)],
                        ),
                       ([pygame.image.load(f'fireball/fireball_diag{i}/fireball_right_down{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_down{i}.png'.format(i)) for i in range(1, 3)],
                        [pygame.image.load(f'fireball/fireball_straight{i}/fireball_down{i}.png'.format(i)) for i in range(1, 3)]
                        )
                       ]

        self.direcctions = [((1, -1), (1, 1), (1, 0)), ((-1, -1), (-1, 1), (-1, 0)), ((1, -1), (-1, -1), (0, -1)),
                            ((1, 1), (-1, 1), (0, 1))]
        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            for i in range(len(self.bullet[self.actions.index(self.current_action)])):
                bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                       self.bullet[self.actions.index(self.current_action)][i],
                                       self.direcctions[self.actions.index(self.current_action)][i]))
            self.choose_action()
        self.animcount += 1
        x = 0
        for i in range(self.lifes):
            pygame.draw.rect(self.sc, pygame.Color('red'), (100 + x, 980, 40, 10))
            x += 40



class ManEater(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load(f'man_eater/man_eater_right/maneater_right{i}.png'.format(i)) for i in range(1, 7)]

        self.left = [pygame.image.load(f'man_eater/man_eater_left/maneater_left{i}.png'.format(i)) for i in range(1, 7)]

        self.up = [pygame.image.load(f'man_eater/man_eater_up/maneater_up{i}.png'.format(i)) for i in range(1, 7)]

        self.down = [pygame.image.load(f'man_eater/man_eater_down/maneater_down{i}.png'.format(i)) for i in range(1, 7)]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = {
                        (1, 0): [pygame.image.load(f'fireball/fireball_straight{i}/fireball_right{i}.png'.format(i)) for i in range(1, 3)],
                        (-1, 0): [pygame.image.load(f'fireball/fireball_straight{i}/fireball_left{i}.png'.format(i)) for i in range(1, 3)],
                        (0, -1): [pygame.image.load(f'fireball/fireball_straight{i}/fireball_up{i}.png'.format(i)) for i in range(1, 3)],
                        (0, 1): [pygame.image.load(f'fireball/fireball_straight{i}/fireball_down{i}.png'.format(i)) for i in range(1, 3)],
                        (1, 1):  [pygame.image.load(f'fireball/fireball_diag{i}/fireball_right_down{i}.png'.format(i)) for i in range(1, 3)],
                        (1, -1): [pygame.image.load(f'fireball/fireball_diag{i}/fireball_right_up{i}.png'.format(i)) for i in range(1, 3)],
                        (-1, 1): [pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_down{i}.png'.format(i)) for i in range(1, 3)],
                        (-1, -1): [pygame.image.load(f'fireball/fireball_diag{i}/fireball_left_up{i}.png'.format(i)) for i in range(1, 3)]
                        }

        self.direcctions = [[[(1, 0)],
                              [(1, -1), (1, 1)],
                              [(1, -1), (1, 1), (1, 0)],
                              [(1, 1), (1, -1), (-1, 1), (-1, -1)]],
                           [[(-1, 0)],
                              [(-1, -1), (-1, 1)],
                              [(-1, -1), (-1, 1), (-1, 0)],
                              [(1, 1), (1, -1), (-1, 1), (-1, -1)]],

                            [[(0, -1)],
                              [(1, -1), (-1, -1)],
                              [(1, -1), (-1, -1), (0, -1)],
                              [(1, 0), (-1, 0), (0, 1), (0, -1)]],

                            [[(0, 1)],
                              [(1, 1), (-1, 1)],
                              [(1, 1), (-1, 1), (0, 1)],
                              [(1, 0), (-1, 0), (0, 1), (0, -1)]]
                            ]

        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            atack = self.direcctions[self.actions.index(self.current_action)][randint(0, 3)]
            for i in range(len(atack)):
                bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                       self.bullet[atack[i]], atack[i]))
            self.choose_action()
        self.animcount += 1
        x = 0
        for i in range(self.lifes):
            pygame.draw.rect(self.sc, pygame.Color('red'), (100 + x, 980, 40, 10))
            x += 40
