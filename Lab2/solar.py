# Alina Chadwick
# CS1 Prof. Balkcom
# Lab 2 - Solar System Lab
# October 2020

#tests code from Body and System classes in a Solar System model

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6        # time scale estimate for graphics
PIXELS_PER_METER = 7 / 1e10  # distance estimate for graphics

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draws the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)


    # Updates the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)




sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 3, 1, .4, 0)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 6, 0, .6, .2)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 7, 0, .4, 1)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 4, .8, .2, 0)
solar_system = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)