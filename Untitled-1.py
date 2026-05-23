from pygame import *

init()

#gamesprite class
class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y,
                 player_speed, width, height):

        super().__init__()

        self.image = transform.scale(
            image.load(player_image),
            (width, height)
        )

        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#player class
class Player(GameSprite):

    # right paddle
    def update_left(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < window_height - self.rect.height:
            self.rect.y += self.speed

    # right paddle
    def update_right(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < window_height - self.rect.height:
            self.rect.y += self.speed


#window set
background = (200, 250, 250)

window_width = 600
window_height = 500

window = display.set_mode((window_width, window_height))
display.set_caption("Ping Pong")


# all objects

# ball
ball = GameSprite(
    'BallPingPong.png',
    300,
    200,
    4,
    50,
    50
)

# left paddle
paddle1 = Player(
    'paddle.png',
    20,
    180,
    7,
    20,
    120
)

# right paddle
paddle2 = Player(
    'paddle.png',
    560,
    180,
    7,
    20,
    120
)


#ball speed
speed_x = 4
speed_y = 4


#clock
clock = time.Clock()
FPS = 60

game = True


#game loop
while game:

    #event
    for i in event.get():

        if i.type == QUIT:
            game = False

    # background
    window.fill(background)

    #paddle movement
    paddle1.update_left()
    paddle2.update_right()

    # ball movement
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    #collison top botom
    if ball.rect.top <= 0:
        speed_y *= -1

    if ball.rect.bottom >= window_height:
        speed_y *= -1

    #left padle
    if sprite.collide_rect(ball, paddle1):

        speed_x = abs(speed_x)

   #right padd;el
    if sprite.collide_rect(ball, paddle2):

        speed_x = -abs(speed_x)


 #object reset
    ball.reset()
    paddle1.reset()
    paddle2.reset()

    display.update()
    clock.tick(FPS)



