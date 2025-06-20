import pygame, sys
pygame.init()

# Window Information
displayw = 1000
displayh = 600
window = pygame.display.set_mode((displayw,displayh))

# Clock
windowclock = pygame.time.Clock()

# Load image
#image = pygame.image.load("foo.png").convert

# Main Class
class MainRun(object):
    def __init__(self,displayw,displayh):
        self.dw = displayw
        self.dh = displayh
        self.Main()

    def Main(self):
        #Put all variables up here
        running = True

        while running:
            #Event Tasking
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    stopped = True


            window.fill((255,255,255)) 
            pygame.display.update()
            windowclock.tick(60)

    
if __name__ == '__init__':
    MainRun()
