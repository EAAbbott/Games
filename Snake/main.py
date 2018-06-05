import random, pygame, sys
from snake import Snake # import snake class
from pygame import locals


FPS = 60
WINDOWRES = (500, 700) # main window resolutiion (h, w)px
BLOCKSIZE = 20 # px size of atomic 'blocks'
GRIDSIZE = 50 # number of blocks making up board 

assert WINDOWRES[0] % BLOCKSIZE == 0, 'non integer number of blocks'
assert WINDOWRES[1] % BLOCKSIZE == 0, 'non integer number of blocks'

KEY_UP = locals.K_w
KEY_DOWN = locals.K_s
KEY_LEFT = locals.K_a
KEY_RIGHT = locals.K_d
KEY_ESC = locals.K_ESCAPE

WHITE = (255, 255, 255)
GREEN = (0, 255, 100)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)



def coordToPx(position):
    pxX, pxY = map(lambda x: (x * BLOCKSIZE), position)
    return (pxX, pxY)
    


def drawItem(colour, position):
    y, x = coordToPx(position)
    pygame.draw.rect(DISPLAY, colour, 
                     (y, 
                      x, 
                      BLOCKSIZE, 
                      BLOCKSIZE))

def drawGrid():
    for y in range(0, WINDOWRES[0], BLOCKSIZE):
        pygame.draw.line(DISPLAY, GREY, (y, 0), (y, WINDOWRES[1]))
    for x in range(0, WINDOWRES[1], BLOCKSIZE):
        pygame.draw.line(DISPLAY, GREY, (0, x), (WINDOWRES[0], x))   
        

def main():
    pygame.init() #initialise
    global FPSCLOCK, DISPLAY
    GAMEOVER = False
    FPSCLOCK = pygame.time.Clock()
    FPSDIV = 1 # some way of running at 60fps but only updating a certain 
                # number of frames
    DISPLAY = pygame.display.set_mode(WINDOWRES)
    pygame.display.set_caption('Snake')
    
    snake = Snake(pos=(5, 3))
    
    fruitLoc = (10, 10)
    

    while not GAMEOVER: #Main game loop
        DISPLAY.fill(BLACK) #refresh every frame
        for event in pygame.event.get():
            if event.type == locals.KEYDOWN:
                if event.key == KEY_UP:
                    snake.setDirection((0, -1))
                if event.key == KEY_DOWN:
                    snake.setDirection((0, 1))
                if event.key == KEY_LEFT:
                    snake.setDirection((-1, 0))
                if event.key == KEY_RIGHT:
                    snake.setDirection((1, 0))
                if event.key == KEY_ESC:
                    GAMEOVER = True
                if event.key == locals.K_e:
                    snake.grow()
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()

        #Redraw and do checks every FPS / 12 = 5 frames
        if (FPS / FPSDIV) == 12:
            
            if snake.locate()[0] >= (WINDOWRES[0] // BLOCKSIZE):
                snake.changePos((0, snake.locate()[1]))
            if snake.locate()[0] < 0:
                snake.changePos(((WINDOWRES[0] // BLOCKSIZE),
                                 snake.locate()[1]))
                
            if snake.locate()[1] >= (WINDOWRES[1] // BLOCKSIZE):
                snake.changePos((snake.locate()[0], 0))
            if snake.locate()[1] < 0:
                snake.changePos((snake.locate()[0],
                                 (WINDOWRES[1] // BLOCKSIZE)))
            
            if snake.locate() == fruitLoc:
                snake.grow()
                fruitLoc = (random.randint(0, (WINDOWRES[0] // BLOCKSIZE) - 1),
                            random.randint(0, (WINDOWRES[1] // BLOCKSIZE) - 1))
            
            #redraw and tick
            snake.move()
            for i in range(len(snake.tail)):
                drawItem(WHITE, snake.tail[i])
            drawItem(GREEN, fruitLoc)
            drawGrid()
            pygame.display.update()
            FPSDIV = 1
        
        
        FPSCLOCK.tick(FPS)
        FPSDIV += 1
        
    pygame.quit()
    sys.exit()
        
if __name__ == '__main__':
    main()

