#-------------------------------------------------------------------------
#
# Begin the Sparks Replication
#-------------------------------------------------------------------------

import pygame
import sys
import random
from pygame.locals import *
pygame.init()

WINDOW_X = 800
WINDOW_Y = 600



total_particles = 0
particles_large = 0
particles_small = 0 
partciles_medium = 0
particles_tiny = 0

LIFETIME = 30

NUM_PARTICLES = 50

LEFT_PADDLE = []
RIGHT_PADDLE = []

for x in range(5):
    LEFT_PADDLE.append(pygame.image.load("LeftPaddle-" + str(x + 1) + ".png"))


for x in range(5):
    RIGHT_PADDLE.append(pygame.transform.flip(pygame.image.load("LeftPaddle-" + str(x + 1) + ".png"), True, False))

# Particle Class. We will be instantiating many of these!
class Particle(object):

    def __init__(self, image, dir_x, dir_y, emit_x, emit_y,  countdown, type):
        self.type = type
        self.x = dir_x
        self.y = dir_y
        self.image = image
        self.alive = True
        self.countdown = countdown
        self.pos = image.get_rect().move(emit_x, emit_y)
        
        if type == 1:
            self.lifetime = 2
        if type == 2:
            self.lifetime = 20
        if type == 3:
            self.lifetime = 40
        if type == 4:
            self.lifetime = 50

        self.steps = 0

    def move(self):
        if self.countdown > 0:
            self.countdown -= 1
        else:
            self.steps += 1
            if self.steps == self.lifetime:
                self.alive = False
            self.pos = self.pos.move(self.x, self.y)


screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))  # set up PyGame Window
black = 0, 0, 0  # black is 0 red, 0 green, 0 blue


def getImage():
    particle_image1 = pygame.image.load("large.png").convert_alpha()
    particle_image2 = pygame.image.load("medium.png").convert_alpha()
    particle_image3 = pygame.image.load("small.png").convert_alpha()
    particle_image4 = pygame.image.load("tiny.png").convert_alpha()

    x = random.randint(1, 100)
    global total_particles
    total_particles += 1

    # Particle ids are hardcoded:
    # Large: 1, Medium: 2. small : 3, tiny: 4

    if x <= 6:
        global particles_large
        particles_large +=1
        return (particle_image1, 1)
    elif x <= 30:
        global particles_tiny
        particles_tiny +=1
        return (particle_image4, 4)
    elif x <= 64:
        global particles_small
        particles_small +=1
        return (particle_image3, 3)
    else:
        global partciles_medium
        partciles_medium +=1
        return (particle_image2, 2)


left_particles = []
for x in range(NUM_PARTICLES):  # create 25 objects
    image, type = getImage()
    p = Particle(image, random.uniform(-8, 3), random.uniform(1, 15), random.randint(230, 240), random.randint(311, 331), random.randint(0, 50), type)
    left_particles.append(p)

right_particles = []
for x in range(NUM_PARTICLES):  # create 25 objects
    image, type = getImage()
    # note: 100 pixels are subtracted in the x direction to account for the flip, the object is ~ 100 pixels wide
    p = Particle(image, random.uniform(-3, 8), random.uniform(1, 15), random.randint(630 - 100, 640 - 100), random.randint(311, 331), random.randint(0, 50), type)
    right_particles.append(p)



mouse_x = 0
mouse_y = 0

paddle_image = 2
running = True

# keep count of frames
count = 0
paddle_count = 0

while running:

    # Debugging Particle Chancce:
    # if total_particles >= 100:
    #     print "Total Particles: " + str(total_particles)
    #     print "Large: " + str(particles_large)
    #     print "Medium: " + str(partciles_medium)
    #     print "Small: " + str(particles_small)
    #     print "Tiny: " + str(particles_tiny)
    #     pygame.quit()

    pygame.mouse.set_visible(1)

    # -- Check for User closing the window, and QUIT in that event ---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos

    screen.fill(black)  # Clear the screen by filling black

    for p in left_particles:
        p.move()
        if p.countdown == 0:
            # calculate new size
            if (p.lifetime != p.steps) and p.type != 1:
                x = float(p.steps) # note float conversion necessary for decimal / percentage
                # note final integer conversion needed for scaling
                new_size = int((p.lifetime - x) / (p.lifetime) * p.image.get_width()) + 5
                screen.blit(pygame.transform.scale(p.image, (new_size, new_size)), p.pos)
                print new_size 
            else: 
                # Large particles need to stay large
                # and original first stage particles do not need scaling
                screen.blit(p.image, p.pos)


            if p.alive == False:
                left_particles.remove(p)
                # create a new particle and append to list
                image, type = getImage()
                o = Particle(image, random.uniform(-8, 3), random.uniform(1,15), random.randint(230, 240), random.randint(311, 331), random.randint(0, 50), type)
                left_particles.append(o)

    for p in right_particles:
        p.move()
        if p.countdown == 0:
            # calculate new size
            if (p.lifetime != p.steps) and p.type != 1:
                x = float(p.steps) # note float conversion necessary for decimal / percentage
                # note final integer conversion needed for scaling
                new_size = int((p.lifetime - x) / (p.lifetime) * p.image.get_width()) + 5
                screen.blit(pygame.transform.scale(p.image, (new_size, new_size)), p.pos)
                print new_size 
            else: 
                # Large particles need to stay large
                # and original first stage particles do not need scaling
                screen.blit(p.image, p.pos)


            if p.alive == False:
                right_particles.remove(p)
                # create a new particle and append to list
                image, type = getImage()
                # note: 100 pixels are subtracted in the x direction to account for the flip, the object is ~ 100 pixels wide
                o = Particle(image, random.uniform(-3, 8), random.uniform(1,15), random.randint(630 - 100, 640 - 100), random.randint(311, 331), random.randint(0, 50), type)
                right_particles.append(o)

    
    # Randomize Paddle Selections

    if count == 3:
        paddle_count = random.randint(1, 5)
        count = 0

    else:
        count += 1

    if paddle_count == 0:
        screen.blit(LEFT_PADDLE[0], (100, 200))
        screen.blit(RIGHT_PADDLE[0], (500, 200))
    elif paddle_count == 2:
        screen.blit(LEFT_PADDLE[1], (100, 200))
        screen.blit(RIGHT_PADDLE[1], (500, 200))
    elif paddle_count == 3:
        screen.blit(LEFT_PADDLE[2], (100, 200))
        screen.blit(RIGHT_PADDLE[2], (500, 200))
    elif paddle_count == 4:
        screen.blit(LEFT_PADDLE[3], (100, 200))
        screen.blit(RIGHT_PADDLE[3], (500, 200))
    else:
        screen.blit(LEFT_PADDLE[4], (100, 200))
        screen.blit(RIGHT_PADDLE[4], (500, 200))




    pygame.display.update()
    pygame.time.delay(15)


pygame.quit()
