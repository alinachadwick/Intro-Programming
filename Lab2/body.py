# Alina Chadwick
# CS1 Prof. Balkcom
# Lab 2 - Solar System Lab
# October 2020

# class Body, creates a celestial body which can be taken in the context of a system

from cs1lib import *

class Body:
    # initial values taken used in the Body class
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass        # mass of body
        self.x = x      # x position of body
        self.y = y      # y position of body
        self.vx = vx        # x velocity of body
        self.vy = vy        # y velocity of body
        self.pixel_radius = pixel_radius        # radius of body
        self.r = r      # color of body, red
        self.g = g      # color of body, green
        self.b = b      # color of body, blue

    # updates position of the body, depending on its velocity and the timestep
    def update_position(self, timestep):
        self.x += self.vx * timestep        # the x position increases depending on the velocity rate of x and the timestep
        self.y += self.vy * timestep        # the y position increases depending on the velocity rate of y and the timestep

    # updates velocity of the body, depending on its acceleration and the timestep
    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep        # the x velocity increases depending on the acceleration rate of x and the timestep
        self.vy += ay * timestep        # the y velocity increases depending on the acceleration rate of x and the timestep

    # draws the body at it's x and y locations
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)      # fill color depends on body parameters
        disable_stroke()        # no outline
        enable_fill()
        draw_circle(self.x*pixels_per_meter + cx, self.y*pixels_per_meter + cy, self.pixel_radius)      # function that physically draws the body
