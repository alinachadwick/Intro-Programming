# Alina Chadwick
# CS1 Professor Balkcom
# Lab 4
# November 2020

from collections import *

def breadth_first_search(START, GOAL):
    path = []       # empty list to begin with
    q = deque()     # deque function imported from collections module
    path_dict = {}      # backpoint dictionary, empty initially
    q.append(START)     # adds START object to deque

    while len(q) != 0:      # while the deque is not empty
        vertex = q.popleft()        # pops vertex off the deque

    # for loop that adds edges to the path dictionary and to the deque
        for edge in vertex.adjacency_list:
            if edge not in path_dict:       # if the edge has not been considered previously
                path_dict[edge] = vertex        # adds the edge to the dictionary as a vertex objecy
                q.append(edge)      # adds edge to deque

    while GOAL != START:
        path.append(GOAL)       # adds the goal to the path list
        GOAL = path_dict[GOAL]      # updates GOAL object

    path.append(START)          # adds START object to the path

    return path