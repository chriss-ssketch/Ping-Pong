from pygame import *

init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


background = (200, 250, 250)

window_width = 600
window_height = 500

window = display.set_mode((window_width, window_height))
display.set_caption("Ping Pong")


ball = GameSprite('BallPingPong.png', 200, 200, 4, 50, 50)

clock = time.Clock()
FPS = 60

game = True

while game:

    for i in event.get():
        if i.type == QUIT:
            game = False

    window.fill(background)

    ball.reset()

    display.update()
    clock.tick(FPS)

