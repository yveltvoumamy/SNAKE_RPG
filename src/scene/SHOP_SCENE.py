from src.scene.MENU import *
from src.landscape.ITEMS import *
from src.landscape.AREAS import *
from src.heroes.SNAKES import *


ITEMS = [Speeder(), Slower(), BusterPoints(), Screamer(), Freezer(), Longer(), Jewish()]
SNAKES = [Snake(), PortalSnake(), HugeFaceSnake(), DiabeticSnake(), GhostSnake(), SpeederSnake()]
AREAS = [SpeedArea(), SlowArea(), GrowArea(), JewishArea()]
stone_heart = LifeHeart()
mountains = RockOnDefaultArea()
apple = Apple()
gode_mode = False
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
sprite = pygame.image.load("pictures/area/default_area.png")
snake = Snake()
current_area = AREAS[randint(0, len(AREAS) - 1)]
new_item = ITEMS[randint(0, len(ITEMS) - 1)]
sc = pygame.display.set_mode([1000, 1000])


class Shop():
    snake, current_area, new_item, gode_mode = None, None, None, None

    def change_snake(self, i):
        #global snake
        print(type(self.snake))
        score = self.snake.SCORE
        lifes = self.snake.lifes
        maxlifes = self.snake.maxlifes
        coeficient = self.snake.coefficient
        self.snake = SNAKES[i]
        self.snake.SCORE = score
        self.snake.lifes = lifes
        self.snake.maxlifes = maxlifes
        self.snake.coefficient = coeficient
        self.snake.reset()
        print(type(self.snake))

    def buy_snake(self):
        showcase = Menu()
        showcase.append_option(SNAKES[5].__class__.__name__ + '      -50$', lambda: self.pay(20, lambda: self.change_snake(5)))
        showcase.append_option(SNAKES[2].__class__.__name__ + '  -50$', lambda: self.pay(50, lambda: self.change_snake(2)))
        showcase.append_option(SNAKES[3].__class__.__name__ + '      -100$', lambda: self.pay(100, lambda: self.change_snake(3)))
        showcase.append_option(SNAKES[1].__class__.__name__ + '          -150$', lambda: self.pay(150, lambda: self.change_snake(1)))
        showcase.append_option(SNAKES[4].__class__.__name__ + '          -200$', lambda: self.pay(200, lambda: self.change_snake(4)))

        shop_alive(showcase)

    def pay(self, num, func):
        #global snake
        if self.gode_mode:
            func()
        elif self.snake.SCORE >= num:
            self.snake.SCORE -= num
            func()

    def upgrade_snake(self):
        showcase = Menu()
        # showcase.append_option('Increase lenght', lambda: snake.changing_lenght(1))
        showcase.append_option('Decrease lenght       -3$', lambda: self.pay(3, lambda: self.snake.changing_lenght(-1)))
        showcase.append_option('Increase speed        -1$', lambda: self.pay(1, lambda: self.snake.changing_speed(1)))
        # showcase.append_option('Decrease speed', lambda: snake.changing_speed(-1))
        showcase.append_option('Increase coefficient -20$', lambda: self.pay(20, lambda: self.changing_coefficient(1)))
        showcase.append_option('Increase maxlifes    -10$', lambda: self.pay(10, lambda: self.snake.changing_maxlifes(1)))

        shop_alive(showcase)

    def changing_coefficient(self, num):
        #global snake
        self.snake.coefficient += 1

    def change_area(self, i):
        #global current_area
       # print(type(current_area))
        self.current_area = AREAS[i]
        self.current_area.new_item([])
        print(type(current_area))

    def buy_area(self):
        showcase = Menu()
        showcase.append_option(AREAS[0].__class__.__name__ + '          -50$', lambda: self.pay(50, lambda: self.change_area(0)))
        showcase.append_option(AREAS[1].__class__.__name__ + '            -50$', lambda: self.pay(50, lambda: self.change_area(1)))
        showcase.append_option(AREAS[2].__class__.__name__ + '           -250 $', lambda: self.pay(250, lambda: self.change_area(2)))
        showcase.append_option('HolyWaterArea  -100$', lambda: self.pay(100, lambda: self.change_area(3)))

        shop_alive(showcase)

    def sell_lenght(self):
        #global snake
        self.snake.changing_lenght(5)
        # snake.SCORE += 2

    def sell_coeficient(self):
        ##global snake
        if self.snake.fps == 1:
            return
        self.snake.fps -= 1
        # snake.SCORE += 1

    def sell_lifes(self):
        #global snake
        if self.snake.lifes == 1:
            return
        self.snake.lifes -= 1
        # snake.SCORE += 25

    def sell_maxlifes(self):
        #global snake
        if self.snake.maxlifes == 1:
            return
        self.snake.maxlifes -= 1
        # snake.SCORE += 75

    def sell_something(self):
        showcase = Menu()
        showcase.append_option('sell snake                             +75$',
                               lambda: self.pay(-75, lambda: self.change_snake(0)) if type(self.snake) != Snake else ...)
        showcase.append_option('Increase lenght for money  +10$', lambda: self.pay(-10, lambda: self.sell_lenght()))
        showcase.append_option('sell coeficient                       +15$',
                               lambda: self.pay(-15, lambda: self.sell_coeficient()) if self.snake.coefficient != 1 else ...)
        showcase.append_option('sell speed                               +1$',
                               lambda: self.pay(-1, lambda: self.sell_speed()) if self.snake.fps != 1 else ...)
        showcase.append_option('sell lifes                                +10$',
                               lambda: self.pay(-10, lambda: self.sell_lifes) if self.snake.lifes != 1 else ...)
        showcase.append_option('sell maxlifes                         +20$',
                               lambda: self.pay(-20, lambda: self.sell_maxlifes()) if self.snake.maxlifes != 1 else ...)

        shop_alive(showcase)

    def pay_to_win(self):
        sc.fill(pygame.Color('black'))
        render_score = font_score.render('YOU WIN', 1, pygame.Color('orange'))
        sc.blit(render_score, (snake.RES // 2 - 50, snake.RES // 2))
        pygame.display.flip()
        sleep(5)

    def spawn_item(self, i):
        #global new_item
        self.new_item = ITEMS[i]
        self.new_item.new_item(list(list(x[0]) for x in mountains.rocks))
        print(ITEMS[i].__class__.__name__)

    def spawn_items(self):
        showcase = Menu()
        showcase.append_option('Spawn Speeder', lambda: self.spawn_item(0))
        showcase.append_option('Spawn Slower', lambda: self.spawn_item(1))
        showcase.append_option('Spawn BusterPoints', lambda: self.spawn_item(2))
        showcase.append_option('Spawn Screamer', lambda: self.spawn_item(3))
        showcase.append_option('Spawn Freezer', lambda: self.spawn_item(4))
        showcase.append_option('Spawn Longer', lambda: self.spawn_item(5))
        showcase.append_option('Spawn Jewish', lambda: self.spawn_item(6))
        showcase.append_option('Spawn StoneHeart', lambda: stone_heart.new_item(list(list(x[0]) for x in mountains.rocks)))

        shop_alive(showcase)

    def changing_gode_mode(self):
        #global gode_mode
        if self.gode_mode:
            self.gode_mode = False
        else:
            self.gode_mode = True

    def scene_SHOP(self, snake, current_area, new_item, gode_mode):
        self.snake = snake
        self.current_area = current_area
        self.new_item = new_item
        self.gode_mode = gode_mode

        shop = Menu()
        shop.append_option('Buy new snake', lambda: self.buy_snake())
        shop.append_option("Upgrade ur snake", lambda: self.upgrade_snake())
        shop.append_option("Change Area", lambda: self.buy_area())
        shop.append_option("Sell something", lambda: self.sell_something())
        shop.append_option("Pay to Win  -1000$", lambda: self.pay(10000, lambda: self.pay_to_win()))
        shop.append_option("", lambda: print('ты че ?'))
        shop.append_option("Gode mode", lambda: self.changing_gode_mode())
        if gode_mode:
            shop.append_option("Spawn Items", lambda: self.spawn_items())
        shop.append_option("", lambda: print('чеееел...'))
        shop.append_option("Battle with Boss", lambda: self.choose_boss(self.snake, self.current_area, self.gode_mode))
        shop_alive(shop)

    def choose_boss(self, snake, current_area, god_mode):
        from src.scene.BATTLE_SCENE import scene_BATTLE
        showcase = Menu()
        showcase.append_option('EyeBall', lambda: scene_BATTLE(snake, current_area, 0, god_mode))
        showcase.append_option('Ghost', lambda: scene_BATTLE(snake, current_area, 1, gode_mode))
        showcase.append_option('BigWorm', lambda: scene_BATTLE(snake, current_area, 2, god_mode))
        showcase.append_option('Pumpking', lambda: scene_BATTLE(snake, current_area, 3, god_mode))
        showcase.append_option('ManEater', lambda: scene_BATTLE(snake, current_area, 4, god_mode))

        shop_alive(showcase)

    def changes(self):
        return self.snake, self.current_area, self.new_item, self.gode_mode


def shop_alive(shop):
    r = True
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                # switch_scene(scene_MENU())
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    shop.switch(-1)
                elif event.key == K_s:
                    shop.switch(1)
                elif event.key == K_SPACE:
                    shop.select()
                elif event.key == K_ESCAPE:
                    # snake, current_area, new_item, gode_mode = self.snake, self.current_area, self.new_item, self.gode_mode
                    return
        sc.fill((0, 0, 0))

        shop.draw(sc, 100, 100, 75)

        display.flip()