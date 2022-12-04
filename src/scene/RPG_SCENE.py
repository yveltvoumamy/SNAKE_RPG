import pygame
from src.landscape.ITEMS import *
from src.landscape.AREAS import *
from src.heroes.SNAKES import *
from src.scene.SHOP_SCENE import Shop

shop = Shop()


class Scene():
    ITEMS = [Speeder(), Slower(), BusterPoints(), Screamer(), Freezer(), Longer(), Jewish()]
    SNAKES = [Snake(), PortalSnake(), HugeFaceSnake(), DiabeticSnake(), GhostSnake(), SpeederSnake()]
    AREAS = [SpeedArea(), SlowArea(), GrowArea(), JewishArea()]

    def __init__(self):
        self.snake = Snake()
        self.sc = pygame.display.set_mode([self.snake.RES, self.snake.RES])
        self.current_area = self.AREAS[randint(0, len(self.AREAS) - 1)]
        self.new_item = self.ITEMS[randint(0, len(self.ITEMS) - 1)]
        self.stone_heart = LifeHeart()
        self.apple = Apple()
        self.gode_mode = False
        self.clock = pygame.time.Clock()
        self.font_score = pygame.font.SysFont('Arial', 26, bold=True)

        self.current_area.new_item([])
        self.snake.reset()
        self.snake.alive = True
        self.apple.new_item(list(list(x[0]) for x in self.mountains.rocks))

    def render_area(self):
        self.sc.fill(pygame.Color('black'))
        for h in range(0, 1040, self.snake.SIZE):
            for w in range(0, 1040, self.snake.SIZE):
               self. sc.blit(self.sprite, (w, h, self.snake.SIZE, self.snake.SIZE))
        self.current_area.render_img()
        self.mountains.render()
        self.apple.render()
        self.stone_heart.run_from(self.snake, self.mountains)
        self.stone_heart.render()
        self.new_item.render()
        self.snake.render()
        render_lifes = self.font_score.render(f'LIFES: {self.snake.lifes} / {self.snake.maxlifes}', 1, pygame.Color('darkred'))
        render_score = self.font_score.render(f'MONEY: {self.snake.SCORE}$', 1, pygame.Color('darkred'))
        render_coeficient = self.font_score.render(f'Coefficient: X{self.snake.coefficient}', 1, pygame.Color('darkred'))
        self.sc.blit(render_lifes, (5, 5))
        self.sc.blit(render_score, (5, 35))
        self.sc.blit(render_coeficient, (5, 65))
        self.stone_heart.spawn(self.mountains)

    def snake_movement(self):
        self.snake.move()
        if not self.gode_mode:
            self.mountains.in_rocks(self.snake)
            self.snake.game_over()

    def spawn_items(self):
        ran = randint(0, 10)
        if not ran and not self.new_item.on_board:
            self.new_item = self.ITEMS[randint(0, len(self.ITEMS) - 1)]
            self.new_item.new_item(list(list(x[0]) for x in self.mountains.rocks))

    def game_rendering(self):
        pygame.display.flip()
        self.clock.tick(self.snake.fps)

    def eating_apple(self):
        if not self.snake.eat(self.apple, self.mountains):
            # in area
            self.current_area.check_in_area(self.snake)
        self.snake.eat(self.new_item, self.mountains)
        self.snake.eat(self.stone_heart, self.mountains)


class Rpg(Scene):
    mountains = RockOnDefaultArea()
    sprite = pygame.image.load("pictures/area/default_area.png")

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and self.snake.direction != Vector2(0, 0):
                    shop.scene_SHOP(self.snake, self.current_area, self.new_item, self.gode_mode)
                    self.snake, self.current_area, self.new_item, self.gode_mode = shop.changes()
                if self.snake.control(event):
                    break

    def game_cycle(self):
        while self.snake.alive:
            self.render_area()
            self.snake_movement()
            self.spawn_items()
            self.game_rendering()
            self.eating_apple()
            self.check_event()

    def start(self):
        self.game_cycle()
        self.snake.write_down_score()
