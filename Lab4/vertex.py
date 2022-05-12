# Alina Chadwick
# CS1 Professor Balkcom
# Lab 4
# November 2020

# Vertex class used to identify locations and paths on Dartmouth campus

from cs1lib import *
class Vertex:
    def __init__(self, name, x, y):     # initial values associated with the object
        self.name = name        # name of vertex
        self.x = int(x)      # x coordinate
        self.y = int(y)      # y coordinate
        self.adjacency_list = []        # empty list used to create edges in a further method

    def __str__(self):      # creates a string of the data associated with the object
        list_of_str = ""        # empty string
        length_of_list = len(self.adjacency_list)

        # for each index in the list, add the index to the string with a comma (except for the last index)
        for index in range(length_of_list - 1):
            list_of_str += self.adjacency_list[index].name + ","
        list_of_str += self.adjacency_list[length_of_list - 1].name     # last vertex does not need a comma
        return str(self.name) + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + list_of_str

    def add_edge(self, edges):      # method that adds edges to the adjacency list
        self.adjacency_list.append(edges)

    def draw_vertex(self, r, g, b):     # method that draws a circle at each vertex
        set_stroke_width(0)
        set_fill_color(r, g, b)     # determines color
        draw_circle(self.x, self.y, VERTEX_RADIUS)      # draws circle

    def draw_edge(self, object, r, g, b):      # method that draws the edges in between vertices
        set_stroke_color(r, g, b)       # determines color
        set_stroke_width(EDGE_WIDTH)        # sets stroke width to 4
        for object in self.adjacency_list:      # for loop that draws lines in between each vertex in adjacency_list
            draw_line(self.x, self.y, object.x, object.y)

    def smallest_surrounding_square(self, x, y):        # determines the smallest square the mouse can be in
        left_bound = self.x - VERTEX_RADIUS        # the left boundary of the smallest square
        right_bound = self.x + VERTEX_RADIUS       # the right boundary of the smallest square
        bottom_bound = self.y - VERTEX_RADIUS      # the bottom boundary of the smallest square
        top_bound = self.y + VERTEX_RADIUS         # the top boundary of the smallest square
        return x < right_bound and x > left_bound and y > bottom_bound and y < top_bound    # within the boundaries

EDGE_WIDTH = 4      # stroke width of edges
VERTEX_RADIUS = 9       # radius of the vertex circles