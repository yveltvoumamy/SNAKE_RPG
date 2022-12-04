from src.scene.MENU import *
from src.landscape.ITEMS import *
from src.landscape.AREAS import *
from src.heroes.SNAKES import *
from src.scene.SHOP_SCENE import *
from src.heroes.BOSSES import *
from src.scene.RPG_SCENE import Scene


def scene_BATTLE(snake, current_area, num_boss, god_mode):
    BATTLE = Battle()
    BATTLE.start(snake, current_area, num_boss, god_mode)


class Battle(Scene):
    mountains = RockOnBosssArea()
    BOSSES = [Eyeball(), Ghost(), BigWorm(), Pumpking(), ManEater()]
    sprite = pygame.image.load("pictures/area/boss_area.png")
    boss = None
    bullets = []

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.snake.alive = exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                self.snake.control(event)

    def boss_ativate(self):
        self.boss.move_from(self.snake)
        self.boss.render(self.bullets)

    def eating_apple(self):
        if not self.snake.eat(self.apple, self.mountains):
            self.current_area.check_in_area(self.snake)
        else:
            self.boss.lifes -= 1
            if self.boss.lifes == 0:
                self.sc.fill(pygame.Color('black'))
                render_score = self.font_score.render('YOU WIN', 1, pygame.Color('orange'))
                self.sc.blit(render_score, (self.snake.RES // 2 - 50, self.snake.RES // 2))
                pygame.display.flip()
                sleep(5)
                self.snake.alive = False

        self.snake.eat(self.new_item, self.mountains)
        self.snake.eat(self.stone_heart, self.mountains)

    def render_bullets(self):
        for bullet in self.bullets:
            bullet.draw(self.sc)

    def check_snake_death(self):
        snake_body = list(list(x) for x in self.snake.body)
        bullets_coords = list(list(s for s in list(x for x in bullet.coordinate)) for bullet in self.bullets)
        if any(x in bullets_coords or x == self.boss.coordinate for x in snake_body):
            if self.snake.lifes == 1:
                self.snake.alive = False
            else:
                self.snake.lifes -= 1
                self.snake.reset()

    def move_bullets(self):
        for bullet in self.bullets:
            if self.snake.RES > bullet.coordinate.x > 0 and 0 < bullet.coordinate.y < self.snake.RES:
                bullet.coordinate.x += bullet.vel[0]
                bullet.coordinate.y += bullet.vel[1]
            else:
                self.bullets.pop(self.bullets.index(bullet))

    def game_sycle(self):
        while self.snake.alive:
            self.move_bullets()
            self.render_area()
            self.render_bullets()
            self.snake_movement()
            self.check_snake_death()
            self.eating_apple()
            self.spawn_items()
            self.boss_ativate()
            self.game_rendering()
            self.check_event()
        self.snake.alive = True

    def start(self, snake, current_area, num_boss, gode_mode):
        self.snake = snake
        self.current_area = current_area
        self.boss = self.BOSSES[num_boss]
        self.gode_mode = gode_mode
        self.snake.reset()
        self.game_sycle()

