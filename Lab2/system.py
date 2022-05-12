# Alina Chadwick
# CS1 Prof. Balkcom
# Lab 2 - Solar System Lab
# October 2020

# creates a System class that takes celestial bodies (from class Body) and combines them into an interactive system

from math import *

GRAVITY = 6.67384e-11

class System:
    def __init__(self, body_list):      #initial values include a list of bodies from class Body
        self.body_list = body_list

    def compute_acceleration(self, n):      # computes the acceleration for each body
        ax = 0      #initial accelerations for x and y are zero
        ay = 0

        for body in self.body_list:
            if body != self.body_list[n]:       # ensures that there will not be calculations of acceleration of 'n' upon itself
                dx = (body.x - self.body_list[n].x)     # calculates distance in x
                dy = (body.y - self.body_list[n].y)     # calculates distance in y
                r = sqrt((dx ** 2) + (dy ** 2))     # uses the pythagorean theorem to find the distance between the two bodies
                a = (GRAVITY * body.mass) /(r*r)        # computes acceleration

                ax_each = (a * dx) / r      # computes acceleration in x per body
                ay_each = (a * dy) / r      # computes acceleration in y per body
                ax += ax_each       # computes the acceleration in x given all of the bodies in play
                ay += ay_each       # computes the acceleration in y given all of the bodies in play
            return ax, ay

    # iterates through every body (object) and calls the update position method, to update the position, and the update velocity method, to update velocity
    def update(self, timestep):

        for body in self.body_list:
            body.update_position(timestep)      #updates the position

        for body in self.body_list:
            n = self.body_list.index(body)
            (ax, ay) = self.compute_acceleration(n)     # calls upon the compute_acceleration method from above
            body.update_velocity(ax, ay, timestep)          #updates the velocity

    # for every body (object in the list) calls it's draw method from Body class
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)