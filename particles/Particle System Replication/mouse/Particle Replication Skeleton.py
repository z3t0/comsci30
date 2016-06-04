#-------------------------------------------------------------------------------
#
# Begin the Sparks Replication
#-------------------------------------------------------------------------------
import pygame, sys, random
from pygame.locals import *
pygame.init()

WINDOW_X = 800
WINDOW_Y = 600

LIFETIME = 30

NUM_PARTICLES = 50

LEFT_PADDLE = []

for x in range(5):
    LEFT_PADDLE.append(pygame.image.load("LeftPaddle-"+str(x+1)+".png"))


#Particle Class. We will be instantiating many of these!
class Particle(object):
    def __init__(self, image, dir_x, dir_y, emit_x, emit_y,  countdown, type):
        self.type = type
        self.x = dir_x
        self.y = dir_y
        self.image = image
        self.alive = True
        self.countdown = countdown
        self.pos = image.get_rect().move(emit_x, emit_y)
        self.lifetime = LIFETIME
        self.steps = 0

    def move(self):
        if self.countdown>0:self.countdown -= 1
        else:
            self.steps += 1
            if self.steps == self.lifetime: self.alive = False
            self.pos = self.pos.move(self.x, self.y)


screen = pygame.display.set_mode((WINDOW_X,WINDOW_Y))     #set up PyGame Window
black = 0,0,0                                             #black is 0 red, 0 green, 0 blue



def getImage():
    particle_image1 = pygame.image.load("large.png").convert_alpha()
    particle_image2 = pygame.image.load("medium.png").convert_alpha()
    particle_image3 = pygame.image.load("small.png").convert_alpha()
    particle_image4 = pygame.image.load("tiny.png").convert_alpha()

    x = random.randint(1, 4)

    if x == 0: return (particle_image, x)
    elif x == 2: return (particle_image2, x)
    elif x == 3: return (particle_image3, x)
    else: return (particle_image4, x)


particles = []
for x in range(NUM_PARTICLES): 		#create 25 objects
    image, type = getImage()
    p = Particle(image,random.uniform(-8,3),random.uniform(1,15),WINDOW_X / 2,WINDOW_Y / 2,random.randint(0,50),type)
    particles.append(p)





mouse_x = 0
mouse_y = 0

paddle_image = 2
running = True


while running:
    pygame.mouse.set_visible(1)

    # -- Check for User closing the window, and QUIT in that event ---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

    screen.fill(black)  # Clear the screen by filling black

    for p in particles:
        p.move()
        if p.countdown == 0:
            screen.blit(p.image, p.pos)
            if p.alive==False:
                particles.remove(p)
                #create a new particle and append to list
                image, type = getImage()
                o = Particle(image,random.uniform(-8,3),random.uniform(1,15),mouse_x,mouse_y,random.randint(0,50),type)
                particles.append(o)

    print str(mouse_x) + " : " + str(mouse_y)

    pygame.display.update()


pygame.quit()


















































































