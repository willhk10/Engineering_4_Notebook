import pygame

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
(width, height) = (200, 300)

running = True

def main():
    global running, screen

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hello World")
    screen.fill(RED)
    pygame.display.update()

    while running:
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                drawCircle()
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    screen = WHITE
                    pygame.display.update()

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawCircle():
    pos=getPos()
    pygame.draw.circle(screen, BLUE, pos, 20) # Here <<<

def makeWhite()
if __name__ == '__main__':
    main()