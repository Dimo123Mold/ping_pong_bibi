from pygame import *
import math
init()

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed, width, height):
        super().__init__()

        self.image = transform.scale(image.load(image1), (width, height))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x ,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 600
win_height = 500
win = display.set_mode((win_width,win_height))
background = transform.scale(image.load("gfh.png"), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("bibi.png", 500, 100, 20, 100, 200)
racket2 = Player("bibi.png", 20, 100, 20, 100, 200)

ball = GameSprite("bacc.png", 300, 200, 10, 70, 70)

font = font.Font(None, 35)
lose1 = font.render(" Бибизяна 1 ПРОПАН!", True, (180, 0, 0))
lose2 = font.render("Бибизяна 2 ПРОПАН!", True, (180, 0, 0))

speed = 5
speedxy = [0, 0]
ang = 15
speedxy[0] = math.cos(math.radians(ang)) * speed
speedxy[1] = math.sin(math.radians(ang)) * speed


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        win.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speedxy[0]
        ball.rect.y += speedxy[1]

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speedxy[0] *= -1

        if ball.rect.y > win_height - 50 or  ball.rect.y < 0:
            speedxy[1] *= -1

        if ball.rect.x < 0:
            finish = True
            win.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            win.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
