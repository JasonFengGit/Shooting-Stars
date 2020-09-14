import pygame as pg
from pygame.locals import *
from time import sleep
import sys
import random

## be in a spaceship!!!
## inspired from
## https://cs.brynmawr.edu/gxk2013/examples/transformations/starfield/
## https://thecodingtrain.com/CodingChallenges/001-starfield.html

width = 500
height = 500
pg.init()
scr = pg.display.set_mode((width, height))
pg.display.set_caption("Shooting Stars")
pg.display.set_icon(scr)

showingMeteors = True

## update the speed of the stars 
def draw():
    speed = (pg.mouse.get_pos()[0] / width) * 10
    for each in stars:
        each.update(speed)
        each.show()

## Star class
class Star:
    # constructor
    def __init__(self):
       self.x = random.randint(-width//2, width//2)
       self.y = random.randint(-height//2, height//2)
       self.z = random.randint(1, width)
       self.oz = self.z

    ## update function
    def update(self, speed):
        self.z -= speed
        
        ## if the star vanished, initialize it again
        if self.z < 1 or self.z == 0:
            self.__init__()

    ## show function
    def show(self):
        sx = int(self.x/self.z * width)
        sy = int(self.y/self.z * height)

        r = int((1 - self.z/width) * 4)
        pg.draw.circle(scr, (255,255,255), (sx + width//2 + r//2, sy + height//2 + r//2), r)

        if(showingMeteors):
            px = int(self.x/self.oz * width)
            py = int(self.y/self.oz * height)
            pg.draw.line(scr, (255,255,255), (sx + width//2, sy + height//2), (px + width//2, py + height//2))

            ## uncomment this line if you want the trail from some distance away
            ## instead of the star's origin position
            #self.oz = self.z + 50
        
## initialize the stars, you may change the number of stars 
num_of_stars = 250
stars = [Star() for i in range(num_of_stars)]

## main loop
while True:
    scr.fill((0,0,0))
    for eve in pg.event.get():
        if eve.type == QUIT:
            sys.exit()
    draw()
    pg.display.update()
    sleep(0.005)
