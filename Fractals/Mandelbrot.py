import pygame
import sys
from numba import jit

XX = 1800       # Screen size X
YY = 900        # Screen size Y
MAXDEPTH = 160  # Maximum iteration count

pygame.init()
screen = pygame.display.set_mode([XX, YY])
screen.set_alpha(None)
screen.fill([0, 0, 0])

pygame.draw.line(screen, [255, 255, 255], [0, YY / 2], [XX, YY / 2], 3)
pygame.draw.line(screen, [255, 255, 255], [XX / 2, 0], [XX / 2, YY], 3)

pygame.display.flip()

x1 = -2     # Initial view top left
y1 = -1
dx = 4      # Initial view size
dy = 2
rechnen = True
surfArray = pygame.surfarray.pixels3d(screen)


@jit
def drawMandelbrotSet(x1, y1, dx, dy, XX, YY, surfArray):
    sx = dx / XX
    sy = dy / YY
    x = x1
    xpos = 0
    while xpos < XX:
        y = y1
        ypos = 0
        while ypos < YY:
            i = mandelbrot(x, y)
            if i == MAXDEPTH:
                color = [0, 0, 0]
            else:
                r = (5 * i) % 255
                g = (7 * i) % 255
                b = (11 * i) % 255
                color = [r, g, b]

            surfArray[xpos][ypos] = color
            y += sy
            ypos += 1
        x += sx
        xpos += 1
        if xpos % 10 == 0:
            pygame.display.flip()


@jit
def mandelbrot(x, y):
    i = 0
    re = x
    im = y
    while i < MAXDEPTH:
        re2 = re * re
        im2 = im * im
        if re2 + im2 > 4:
            break

        im = 2 * re * im + y
        re = re2 - im2 + x
        i += 1
    return i


while True:
    if rechnen:
        drawMandelbrotSet(x1, y1, dx, dy, XX, YY, surfArray)
        rechnen = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                alpha = float(pos[0]) / XX
                beta = float(pos[1]) / YY
                mx = x1 + alpha * dx
                my = y1 + beta * dy
                x1 = mx - dx / 10
                y1 = my - dy / 10
                dx /= 5.0
                dy /= 5.0
                rechnen = True
            else:
                x1 = x1 - 2 * dx
                y1 = y1 - 2 * dy
                dx *= 5.0
                dy *= 5.0
                rechnen = True
