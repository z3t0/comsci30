#-------------------------------------------------------------------------
#
# Ballistics. Create Cannonball particles that reasonably observe the laws of Physics!
#-------------------------------------------------------------------------

import pygame
import sys
import random
import math
from pygame.locals import *
from math import *
pygame.init()

# Lets me make up objects


class Foo(object):
    pass

WINDOW_X = 800
WINDOW_Y = 600

screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))  # set up PyGame Window
black = 0, 0, 0

# Game state
paused = False

# X,Y Coordinates for where to draw the cannon
CANNON_X = 30
CANNON_Y = 425

# Cannonball storage
cannonball_count = 20

GRAVITY = 0.8
POWER_CONSTANT = 3

# Text objects
my_font = pygame.font.SysFont("monospace", 25)
report = my_font.render("My text will say this", 1, (0, 0, 0))
paused_text = my_font.render("Game over. Press Enter to Play again", 1, (0.5, 0, 0))

# Load the cannonball image
cannonball = pygame.image.load("Cannonball.png")

# Load the background images
background = pygame.image.load("Background.png")
background_pos = background.get_rect()
background_report = pygame.image.load("Background-report.png")
background_report_pos = background_report.get_rect()

# Load a list of sprite images for the smoke
smoke_img = []
for x in range(4):
    smoke_img.append(pygame.image.load("smoke" + str(x+1) +".png"))

class Particle(object):
    def __init__(self, x, y):
        self.image = 0
        self.x = x
        self.y = y
        self.alive = True

    def move(self):
        self.x = rand.randint(self.x - 5, self.x + 5)
        self.y = rand.randint(self.y + 1, self.y + 10)

        if self.image == 4
            self.alive = False

        else:
            self.image = random.randint(self.image, 4)



class Smoke (object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.particles = []

        for x in range(100):
            self.particles.append((0, smoke_img[0]))

    def move(self):
        for p in self.particles:
            t = particles [p]

            num = t[0]
            img = t[1]

            if num == 4:
                particles.remove(p)
            else:
                i = random.randint(num, 3) # next sprite
                particles.remove(p)
                x = random.randint(self.x - 5, self.x + 5)                
                y = random.randint(self.x, self.y + 5)                
                particle = smoke_img[i].move(x, y)
                new_t = (i, particle)
                particles.append(new_t)


smoke_example = Smoke(200,200)

# Load a list of sprite images for the cannon ball counter
cannonball_count_gui = []
for x in range(20):
    cannonball_count_gui.append(pygame.image.load("shots" +str(x+1) + ".png"))

# Load a list of sprite images for the Cannon
cannon = []
for x in range(7):
    cannon.append(pygame.image.load("Cannon-" + str(x * 15) + ".png"))

# Load a list of sprite images for explosions
explosion_img = []
for x in range(6):
    explosion_img.append(pygame.image.load("ex" + str(x+1) + ".png"))

explosions = []

class Explosion(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = 0
        self.alive = True
        self.anim = 0 # modifies animation speed by half

    def next_image(self):
        if self.anim == 1:
            self.image +=1
            self.anim = 0
        else:
            self.anim = 1

        if self.image == 5:
            self.alive = False

# Load a list of sprite images for the power GUI
power = Foo()
power.image = []
for x in range(10):
    power.image.append(pygame.image.load("power" + str(x+1) + ".png"))

power.count = 1

# Load a list of sprite iamges for the target GUI
target = Foo()
target.image = []
for x in range(20):
    target.image.append(pygame.image.load("target" + str(x+1) + ".png"))

target.target = pygame.image.load("target.png")

target.count = 0
target.hit = False
# the region of x, y values are within the shooting area, in front of the cannon,
# and above the ground

# spawns target
def spawn():
    target.pos = target.target.get_rect()
    target.pos.x = random.randint(200, 800)
    target.pos.y = random.randint(90, 540)

spawn() # spawns initial target

# We will limit possible shooting angles. A list will correspond with
# sprite images from cannon[]
angles = [0, 15, 30, 45, 60, 75, 90]


cannon_image = 2
running = True

# Cannonball class - one instance of this class created per shot


class Ball(object):

    def __init__(self, image, dir_x, dir_y, emit_x, emit_y):
        self.x = dir_x * POWER_CONSTANT * power.count
        self.y = dir_y * POWER_CONSTANT * power.count
        self.image = image
        self.pos = image.get_rect().move(emit_x, emit_y)
        self.alive = True
        self.will_collide = 0  # flag for if the cannon will hit ground next frme
        self.hit_target = 0  # flag for whether the cannonball will hit the target

    def move(self):
        if self.pos.colliderect(target.pos):
            self.hit_target = 1
            target.count += 1 # add to target counter
            explosions.append(Explosion(target.pos.x, target.pos.y))
            spawn() # spawn new target
            self.alive = False

        if self.will_collide == 1:
            self.pos.bottom = 558
            self.pos.x += self.x
            self.alive = False

        else:
            self.y += GRAVITY
            self.pos = self.pos.move(self.x, self.y)
            if (self.pos.bottom + self.y) > 557:
                self.will_collide = 1
            
shots = []

while running:
    pygame.mouse.set_visible(1)

    # -- Check for User closing the window, and QUIT in that event ---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for keyboard input, and change trajectory and power input
        # based on arrow key presses. Space for shoot
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if cannon_image < 6:
                    cannon_image += 1
            if event.key == pygame.K_RIGHT:
                if cannon_image > 0:
                    cannon_image -= 1
            if event.key == pygame.K_DOWN:
                if power.count > 1:
                    power.count -=1
            if event.key == pygame.K_UP:
                if power.count < 10:
                    power.count +=1
            if event.key == pygame.K_SPACE:
                y = (2 * sin(math.radians(angles[cannon_image])))
                x = sqrt((4) - (y * y))
                c = Ball(cannonball, x, y * -1, 95, 515)
                # fire by adding to the list of current shots
                shots.append(c)
                cannonball_count -= 1

    if paused == True:
        # Game is paused
        screen.blit(background_report, background_report_pos)
        screen.blit(paused_text, (200, 250))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                paused = False
                cannonball_count = 20
                target.count = 0
                spawn() # spawn new target

    else:
        if cannonball_count < 1:
            paused = True

        # Clear the screen by filling with out background image
        screen.blit(background, background_pos)

        # GUI
        screen.blit(power.image[power.count - 1], (20, 10))
        screen.blit(cannonball_count_gui[cannonball_count - 1], (280, 30))
        if target.count > 0:
            screen.blit(target.image[target.count - 1], (500, 30))
        screen.blit(report, (200, 250))

        # add target
        screen.blit(target.target, (target.pos.x, target.pos.y))

        screen.blit(explosion_img[0], (200, 200))


        # add cannonball animation
        for s in shots:
            screen.blit(s.image, s.pos)
            s.move()
            if s.alive == False:
                shots.remove(s)


        # render explosions
        for x in explosions:
            screen.blit(explosion_img[x.image], (x.x, x.y))
            x.next_image()
            if x.alive == False:
                explosions.remove(x)

        # Smoke rendering


        cannon_location = cannon[cannon_image].get_rect().move(CANNON_X, CANNON_Y)
        screen.blit(cannon[cannon_image], cannon_location)

    # Update the display and delay for animation
    pygame.display.update()
    pygame.time.delay(10)


pygame.quit()
