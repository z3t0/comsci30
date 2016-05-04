#-------------------------------------------------------------------------------
# Particle System Skeleton Code
#-------------------------------------------------------------------------------

import pygame, sys, random
pygame.init()

WINDOW_SIZE = 800, 600
NUM_PARTICLES = 25

screen = pygame.display.set_mode(WINDOW_SIZE)   #  Set the size of the window

black = 0,0,0   # Black is made up of 0 Red, 0 Green, and 0 Blue

class Particle:
    def __init__(self, image):
        self.x = random.uniform(1, 10)
        self.y = random.uniform(-1, -10)
        self.image = image
        self.pos = image.get_rect().move(100, 500)

    def move(self):
        self.pos = self.pos.move(self.x, self.y)

particle_image = pygame.image.load('p1.png').convert_alpha()
particles = []

for x in range(0, NUM_PARTICLES):
    p = Particle(particle_image)
    particles.append(p)

running = True

while running:  #Main animation loop continues until window close event is encountered

    for event in pygame.event.get():        #  These three lines allow us to
        if event.type == pygame.QUIT:       #  close the program window without
            running = False                 #  Python wanting to crash.

    screen.fill(black)                  #from our Pseudo-code: Fill the screen - this covers up any previously drawn particles and lets us start fresh

    for p in particles:
        p.move
        screen.blit(p.image,  p.pos)

    screen.blit(circle,position)        #Blit (or change pixel colors at the current position of our particle)

    pygame.display.update()             #update the screen to reflect the new changes
    pygame.time.delay(25)



pygame.quit()       #close gracefully, if possible!

