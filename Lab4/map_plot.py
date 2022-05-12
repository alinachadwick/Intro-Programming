# Alina Chadwick
# CS1 Professor Balkcom
# Lab 4
# November 2020

from bfs import *
from vertex import *
from load_graph import *
from cs1lib import *

START = 0
GOAL = 0
startx = 0
starty = 0
EDGE_WIDTH = 4
vertex_dict = load_graph("dartmouth_graph.txt")
image = load_image("dartmouth_map.png")
count = 0

def draw_edges():       # uses draw_edge method to draw all of the edges and vertices in blue
    for vertex in vertex_dict:      # for each vertex in the dictionary, draw vertices in blue
        vertex_dict[vertex].draw_vertex(0, 0, 1)

        vertex = vertex_dict[vertex]
        for edge in vertex.adjacency_list:      # for each edge in the adjacency list, draw edges in blue
            vertex.draw_edge(edge, 0, 0, 1)

def start(x, y):        # start function that is used to determine the first, starting vertices
    global START
    draw_image(image, 0, 0)     # initially draws the image
    draw_edges()            # initially draws edges as well
    for index in vertex_dict:       # loops over each item in the vertex dictionary
        if vertex_dict[index].smallest_surrounding_square(x, y):    # if the mouse is in the smallest surrounding square
            vertex_dict[index].draw_vertex(1, 0, 0)     # a vertex is drawn in red
            START = vertex_dict[index]      # new start variable

def goal(x, y):     # goal function that is used to determine the goal vertices
    global GOAL
    draw_image(image, 0, 0)     #initially draws the image
    draw_edges()            #initially draws the edges as well
    start(startx, starty)     # calls start function
    for index in vertex_dict:       # loops over each item in the vertex dictionary
        if index != START and vertex_dict[index].smallest_surrounding_square(x, y):     # if the index is not the start one and the mouse is in the smallest surrounding square
            vertex_dict[index].draw_vertex(1, 0, 0)     # goal vertex drawn in red
            GOAL = vertex_dict[index]

def draw_path(START, GOAL):
    path = breadth_first_search(START, GOAL)        # uses breadth first search function to create a path
    for index in range(len(path)):      # loops over the length of the path
        path[index].draw_vertex(1, 0, 0)        # draws the vertices in that path

        if index < len(path) - 1:       # if the index is less than the path - 1, the path must be drawn
            set_stroke_width(EDGE_WIDTH)    # sets path width
            set_stroke_color(1, 0, 0)       # sets path color to red
            draw_line(path[index].x, path[index].y, path[index + 1].x, path[index + 1].y)   # draws the path between the index and the one following it

def main():     # main graphics function
    global count, startx, starty, GOAL
    x = mouse_x()       # mouse coordinates for x
    y = mouse_y()       # mouse coordinates for y

    if count == 0:
        draw_image(image, 0, 0)     # draws image
        count += 1

    draw_edges()        # draws all edges onto the image

    if is_mouse_pressed():      # connects start function with mouse input
        start_x = x
        start_y = y
        start(start_x, start_y)

    if START != 0 and GOAL != 0:
        draw_path(START, GOAL)      # path is drawn as long as the start and goal vertices are not equal to zero

start_graphics(main, width=1012, height=811, mouse_press=start, mouse_move=goal)