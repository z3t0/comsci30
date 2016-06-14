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

    def __init__(self, emit_x, emit_y):
        self.type = random.randint(1, 4)
        self.x = random.randint(-5, 5)
        self.y = -3
        self.image = smoke_img[self.type - 1]
        self.alive = True
        self.pos = self.image.get_rect().move(emit_x, emit_y)
        if self.type == 1:
            self.lifetime = random.randint(15,25)
            self.size = 25
        if self.type == 2:
            self.lifetime = random.randint(20,30)
            self.size = 20
        if self.type == 3:
            self.lifetime = random.randint(20,30)
            self.size = 10
        if self.type == 4:
            self.lifetime = random.randint(20,35)
            self.size = 10

        self.countdown = random.randint(0,5)

        self.steps = 0

    def move(self):
        if self.countdown > 0:
            self.countdown -= 1
        else:
            self.steps += 1
            if self.steps == self.lifetime:
                self.alive = False
            self.x = random.randint(-3, 3)
            self.pos = self.pos.move(self.x, self.y)

# Hold all smoke particle lists
smoke = []

class Smoke(object):
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.count = 0
        self.max_count = 800 # about 6 seconds
        self.delete = False
        self.particles = []


        for x in range(100):
            self.particles.append(Particle(self.x, self.y))
            self.count +=1
        smoke.append(self)



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
    target.pos.x = random.randint(200, 700)
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
            self.pos.bottom = 577
            self.pos.x += self.x
            self.alive = False
            self.smoke = Smoke(self.pos.x, 540)
            
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

    if paused == True and len(shots) < 1:
        # Game is paused
        screen.blit(background_report, background_report_pos)
        screen.blit(paused_text, (200, 250))

        # Create Report
        report1 = my_font.render("In 20 shots, you hit " + str(target.count) + " targets.", 1, (0, 0, 0))
        percentage = round(target.count  * 1.0 / 20 * 100)
        report2 = my_font.render("That is " + str(percentage) + "% accuracy", 1, (0, 0, 0))
        
        if percentage >= 95:
            grade = "A +"
        elif percentage >= 85:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >=60:
            grade = "C"
        elif percentage >=50:
            grade = "D"
        elif percentage >=30:
            grade = "E"
        else:
            grade = "F"
        report3 = my_font.render("GRADE " + grade, 1, (0, 0, 0))

        screen.blit(report1, (200, 350))
        screen.blit(report2, (200, 400))
        screen.blit(report3, (200, 450))


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
        if cannonball_count > 0:
            screen.blit(cannonball_count_gui[cannonball_count - 1], (280, 30))
        if target.count > 0:
            screen.blit(target.image[target.count - 1], (500, 30))
       
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


    # Smoke and cannon rendering : outside of loop so it can continue during pause screen
    cannon_location = cannon[cannon_image].get_rect().move(CANNON_X, CANNON_Y)
    screen.blit(cannon[cannon_image], cannon_location)

    for x in smoke:
        for p in x.particles:
                screen.blit(pygame.transform.scale(p.image, (p.size, p.size)), p.pos)
                p.move()
                if p.alive == False:
                    x.particles.remove(p)
                    x.particles.append(Particle(x.x, x.y))
                    x.count += 1
                if x.count >= x.max_count:
                    x.delete = True

    # Create new list for smoke
    new_list = []
    for x in smoke:
        if x.delete == True:
            pass
        else:
            new_list.append(x)

    smoke = new_list

    # Update the display and delay for animation
    pygame.display.update()
    pygame.time.delay(10)


pygame.quit()
