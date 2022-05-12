# Alina Chadwick
# CS1 Prof. Balkcom
# Lab 1 September/October 2020

from cs1lib import *
from random import randint

# main function to input into start_graphics
def pong_graphics():
    paddle_graphics()
    ball_graphics()
    start_game()

# begins the game when the space bar is pressed or when the ball goes out of the x bounds
# resets the location of the paddles and the ball to the initial position
def start_game():
    global y1, y2, x_circle, y_circle, velocity_y, velocity_x
    if pressed_space == True or x_circle > 400 or x_circle < 0:
        y1 = 0
        y2 = 320
        x_circle = 200
        y_circle = 200
        velocity_x = randint(1, 6)
        velocity_y = randint(1, 6)
        x_circle += velocity_x
        y_circle += velocity_y

# function that controls the paddles, draws the background, and allows for movement
def paddle_graphics():
    global x1, x2, y1, y2
    clear()
    set_clear_color(1, 1, 1)    #white background

    set_fill_color(1, 0, 1)     #purple paddles
    draw_rectangle(x1, y1, WIDTH, HEIGHT)   #paddle 1
    draw_rectangle(x2, y2, WIDTH, HEIGHT)   #paddle 2


    # if the key "a" is pressed and the y1 coordinate is above 0, the left paddle will move down by 8 pixels
    if pressed_A == True:
        if y1 > Y_MIN:
            y1 += MOVEMENT_RATE * (-1)

    # if the key "z" is pressed and the y1 coordinate is below 320, the left paddle will move up by 8 pixels
    if pressed_Z == True:
        if y1 < Y_MAX:
            y1 += MOVEMENT_RATE

    # if the key "k" is pressed and the y2 coordinate is above 0, the right paddle will move down by 8 pixels
    if pressed_K == True:
        if y2 > Y_MIN:
            y2 += MOVEMENT_RATE * -1

    # if the key "m" is pressed and the y2 coordinate is below 320, the right paddle will move up by 8 pixels
    if pressed_M == True:
        if y2 < Y_MAX:
            y2 += MOVEMENT_RATE


# function that draws the ball and allows for ball movement across the screen
def ball_graphics():
    global x_circle, y_circle, velocity_y, velocity_x
    set_fill_color(0, 1, 1)     # aqua marine color
    draw_circle(x_circle, y_circle, 6)      # circle at (200, 200) with a radius of 6
    x_circle += velocity_x      # the x coordinate of the ball changes depending on the velocity of x
    y_circle += velocity_y      # the y coordinate of the ball changes depending on the velocity of y

    #if the ball hits the top or bottom of the screen, it changes direction
    if y_circle > 400 or y_circle < 0:
        velocity_y = -1 * velocity_y


    # if the ball hits the left paddle, it changes direction
    if x_circle - 6 < x1 + WIDTH:                       # if the edge of the ball collides with the right edge of the left paddle
        if y_circle > y1 and y_circle < y1 + HEIGHT:    # and if it is between the top and bottom coordinates of the left paddle
            velocity_x = -1 * velocity_x

    # if the ball hits the right paddle, it changes direction
    if x_circle - 6 > x2 - WIDTH:                       # if the edge of the ball collides with the left edge of the right paddle
        if y_circle >= y2 and y_circle <= y2 + HEIGHT:  # and if it is between the top and bottom coordinates of the right paddle
            velocity_x = -1 * velocity_x


#when a key is pressed, the pressed function becomes true
def key_movement(key):
    global pressed_A, pressed_Z, pressed_K, pressed_M, pressed_space
    if key == "a":
        pressed_A = True
    if key == "z":
        pressed_Z = True
    if key == "k":
        pressed_K = True
    if key == "m":
        pressed_M = True
    if key == " ":
        pressed_space = True
    if key == "q":
        cs1_quit()      #the q key quits the function

#when a key is released, the pressed function becomes false
def key_stop(key):
    global pressed_A, pressed_Z, pressed_K, pressed_M, pressed_space
    if key == "a":
        pressed_A = False
    if key == "z":
        pressed_Z = False
    if key == "k":
        pressed_K = False
    if key == "m":
        pressed_M = False
    if key == " ":
        pressed_space = False

x1 = 0          #initial x coordinate for paddle 1
y1 = 0          #initial y coordinate for paddle 1
x2 = 380        #initial x coordinate for paddle 2
y2 = 320        #initial y coordinate for paddle 2
MOVEMENT_RATE = 8   #when a key is pressed, the paddle moves up or down by 8 pixels at a time
WIDTH = 20
HEIGHT = 80

X_MAX = 400     #maximum x value of the window
Y_MAX = 320     #maximum y value for the paddle to be located at
X_MIN = 0       #minimum x value of the window
Y_MIN = 0       #minimum y value for the paddle to be located at
pressed_A = False   #the key "a" moves the left paddle up
pressed_Z = False   #the key "z" moves the left paddle down
pressed_K = False   #the key "k" moves the right paddle up
pressed_M = False   #the key "m" moves the right paddle down
pressed_space = False   #the space key restarts the game
x_circle = 200      #x coordinate of the ball
y_circle = 200      #y coordinate of the ball
velocity_x = randint(1, 6)  #the velocity of x coordinate of the ball is a random number between 1 and 6
velocity_y = randint(1, 6)  #the velocity of y coordinate of the ball is a random number between 1 and 6


start_graphics(pong_graphics, key_press = key_movement, key_release=key_stop)