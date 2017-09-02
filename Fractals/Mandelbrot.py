import pygame
import math
import sys
import cmath

XX=900
YY=600

pygame.init()
screen = pygame.display.set_mode([XX, YY])
screen.fill([0, 0, 0])

pygame.draw.line(screen, [255, 255, 255], [0, YY/2], [XX, YY/2],3)
pygame.draw.line(screen, [255, 255, 255], [XX/2, 0], [XX/2, YY],3)

#pygame.draw.circle(screen, [150, 150, 150], [500, 500],250, 2)
pygame.display.flip()

x1 = -1.5
x2 = 1.5
y1=-1.0
y2=1.0
rechnen = True

while True:
    if rechnen:
        dx = x2 - x1
        dy = y2 - y1
        sx = dx / XX
        sy = dy / YY
        x = x1
        xpos = 0
        while x <= x2:
            y = y1
            ypos = 0
            while y <= y2:
                z = complex(0,0)
                c = complex(x, y)
                for i in range(100):
                    z = z * z + c
                    if abs(z) > 2:
                        break
                if abs(z) < 2:
                    color = [0,0,0]
                else:
                    r = (10 * i) % 255
                    g = (13 * i) % 255
                    b = (16 * i) % 255
                    color = [r, g, b]

                screen.set_at((xpos, ypos), color)

                y = y + sy
                ypos = ypos + 1
            pygame.display.flip()
            x = x + sx
            xpos = xpos + 1
        rechnen = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                alpha = float(pos[0])/ XX
                betha = float(pos[1])/ YY
                mx = x1 + alpha * dx
                my = y1 + betha * dy
                x1 = mx - dx/ 10
                x2 = mx + dx / 10
                y1 = my - dy / 10
                y2 = my + dy / 10
                rechnen = True
            else:
                x1 = x1 - 2 * dx
                x2 = x2 + 2 * dx
                y1 = y1 - 2 * dy
                y2 = y2 + 2 * dy
                rechnen = True