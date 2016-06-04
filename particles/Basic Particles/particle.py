#-------------------------------------------------------------------------------
# Particle System Skeleton Code
#-------------------------------------------------------------------------------

import pygame, sys, random
pygame.init()

WINDOW_SIZE = 800, 600
NUM_PARTICLES = 125

screen = pygame.display.set_mode(WINDOW_SIZE)   #  Set the size of the window

black = 0,0,0   # Black is made up of 0 Red, 0 Green, and 0 Blue

class Particle:
    def __init__(self, image,):
        self.countdown = random.randint(0,10)
        self.x = random.uniform(1, 10)
        self.y = random.uniform(-1, -10)
        self.image = image
        self.pos = image.get_rect().move(100, 500)
        self.lifetime = 40
        self.alive = True

    def move(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.alive = False

        self.pos = self.pos.move(self.x, self.y)

def getImage():
    num = random.randint(0,3)
    return images[num]

images = []
images.append(pygame.image.load('p1.png').convert_alpha())
images.append(pygame.image.load('p2.png').convert_alpha())
images.append(pygame.image.load('p3.png').convert_alpha())
images.append(pygame.image.load('p4.png').convert_alpha())

particles = []

for x in range(0, NUM_PARTICLES):
    p = Particle(getImage())
    particles.append(p)

running = True

while running:  #Main animation loop continues until window close event is encountered

    for event in pygame.event.get():        #  These three lines allow us to
        if event.type == pygame.QUIT:       #  close the program window without
            running = False                 #  Python wanting to crash.

    screen.fill(black)                  #from our Pseudo-code: Fill the screen - this covers up any previously drawn particles and lets us start fresh

    for p in particles:
        if p.countdown < 0:
            p.move()
            screen.blit(pygame.transform.scale(p.image, (p.lifetime, p.lifetime)),  p.pos)

        else:
            p.countdown -= 1

        if p.alive == False:
            particles.remove(p)
            new  = Particle(getImage())
            particles.append(new)

    pygame.display.update()             #update the screen to reflect the new changes
    pygame.time.delay(25)



pygame.quit()       #close gracefully, if possible!

