from pygame import *
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
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

class Ball(GameSprite):
    def update(self, angle):
        self.rect.x += speed_x
        self.rect.y += speed_y
        self.image = transform.rotate(self.image, angle)

back = (255, 200, 255)
win_widgth = 1300
win_height = 700
window = display.set_mode((win_widgth, win_height))
window.fill(back)
bg = transform.scale(image.load("back.jpg"), (win_widgth, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 10, 50, 150) 
racket2 = Player('racket.png', 1250, 200, 10, 50, 150)
ball = Ball('ball.png', 200, 200, 10, 50, 50)

score_p1 = 0
score_p2 = 0

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE! PLAYER 2 WIN!', True, (4, 4, 46))
lose2 = font.render('PLAYER 2 LOSE! PLAYER 1 WIN!', True, (4, 4, 46))
score = font.render(str(score_p1) + ':' + str(score_p2), True, (4, 4, 46))

speed_x = 10
speed_y = 10
score_p1 = 0
score_p2 = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        window.blit(bg, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.update(-90)
        window.blit(score, (500, 50))
        score = font.render(str(score_p1) + ':' + str(score_p2), True, (4, 4, 46))


    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1.1

    if ball.rect.x < 0:
        score_p2 += 1
        ball.rect.x = 650
        ball.rect.y = 340
    if ball.rect.x > win_widgth:
        score_p1 += 1
        ball.rect.x = 650
        ball.rect.y = 340 

    if score_p1>3:
        finish = True
        window.blit(lose2, (120, 200))
    if score_p2>3:
        finish = True
        window.blit(lose1, (120, 200))

    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)