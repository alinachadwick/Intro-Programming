# Alina Chadwick
# CS1 Prof. Balckom
# Lab 3 - City class
# October/November 2020

from cs1lib import *

WINDOW_HEIGHT = 360
WINDOW_WIDTH = 720

count = 0       # initially information has been added to any list or file

img = load_image("world.png")       # imports map of the world

text_file = open("cities_pop.txt", "r")     # opens file with cities sorted based on population, high to low
list_of_cities_latitude = []        # empty list, will be appended with latitudes
list_of_cities_longitude = []       # empty list, will be appended with longitudes

# for loop that appends information from the text file into the lists of city longitudes and latitudes
for line in text_file:
    if count < 50:      # only accounts for the 50 most populous cities in the world
        file_line = line.strip().split(",")      # strips the line of whitespace and splits it into list indices
        longitude_in_pixels= WINDOW_WIDTH / 2 + 2* float(file_line[3])      # converts longitudes to pixels
        latitude_in_pixels = WINDOW_HEIGHT - (2*(float(file_line[2]))+ WINDOW_HEIGHT/2)     # converts latitudes to pixels

        list_of_cities_latitude.append(latitude_in_pixels)      #appends the latitude values to the list
        list_of_cities_longitude.append(longitude_in_pixels)        # appends the longitude values to the list

text_file.close()       # closes the file

count = 0       # initially information has been added to any list or file
index = 0       # initial index

# draws cities at appropriate latitudes and longitudes, one at a time
def draw_cities():
    global count, index
    if count == 0:      # initial condition
        draw_image(img, 0, 0)       # draws map as given
        count+=1

    if index < 50:      # only accounts for the 50 most populous cities in the world
        set_fill_color(1, 0, 1)     #  purple
        draw_circle(list_of_cities_longitude[index], list_of_cities_latitude[index], 3)     # draws circle of radius 3 at each longitude and latitude in the longitude and latitude lists
        index +=1
        count +=1

start_graphics(draw_cities, width= WINDOW_WIDTH, height= WINDOW_HEIGHT, framerate=5)