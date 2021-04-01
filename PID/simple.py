import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rocket Thrust controller')

i = 0


def pid_value(e, e_prev, del_t):
    global i

    Kp = 5
    Kd = 5
    Ki = 5

    p = Kp*e
    d = Kd*((e-e_prev)/del_t)
    i = i + Ki*e*del_t

    return p+d+i


# initialise player
player_img = pygame.image.load('assets/player.png')


def player(x, y):
    # we will use blit function to draw the image on the screen
    screen.blit(player_img, (x, y))


def simulation():

    m = 1
    g = 9.8

    # set point
    target = 400

    # random initialization
    f = 0
    y = 0
    u = 0
    e_prev = target - y

    for _ in range(10000):
        screen.fill((0, 0, 0))
        print(y)
        e = target - y
        del_t = 0.001
        co = pid_value(e, e_prev, del_t)
        new_F = co
        # new data after 1sec
        v = u + ((new_F/m)-g)*del_t
        new_y = y + u*del_t + (0.5*((new_F/m)-g))*(del_t**2)
        # update
        f = new_F
        e_prev = target-y
        y = new_y
        u = v
        player(370, 530 - y)
        pygame.display.update()


simulation()
