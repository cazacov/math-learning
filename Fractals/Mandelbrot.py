import pygame
import sys
from numba import jit

XX = 1200
YY = 900

pygame.init()
screen = pygame.display.set_mode([XX, YY])
screen.set_alpha(None)
screen.fill([0, 0, 0])

pygame.draw.line(screen, [255, 255, 255], [0, YY / 2], [XX, YY / 2], 3)
pygame.draw.line(screen, [255, 255, 255], [XX / 2, 0], [XX / 2, YY], 3)

pygame.display.flip()

x1 = -2
y1 = -1.5
dx = 4
dy = 3
rechnen = True
surfArray = pygame.surfarray.pixels3d(screen)

@jit
def drawMandelbrotSet(x1,y1,dx,dy,XX,YY,surfArray):
    sx = dx / XX
    sy = dy / YY
    x = x1
    xpos = 0
    while xpos < XX:
        y = y1
        ypos = 0
        while ypos < YY:
            i = mandelbrot(x, y)
            if i == 100:
                color = [0, 0, 0]
            else:
                r = (10 * i) % 255
                g = (13 * i) % 255
                b = (16 * i) % 255
                color = [r, g, b]

            surfArray[xpos][ypos] = color
            y += sy
            ypos += 1

        pygame.display.flip()
        x += sx
        xpos += 1


@jit
def mandelbrot(x, y):
    z = complex(0, 0)
    c = complex(x, y)
    i = 0
    while i < 100:
        z = z * z + c
        if z.real * z.real + z.imag * z.imag > 4:
            break
        i += 1
    return i


while True:
    if rechnen:
        drawMandelbrotSet(x1,y1,dx,dy,XX,YY,surfArray)
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
