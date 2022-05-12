# Alina Chadwick
# CS1 Professor Balkcom
# Lab 4
# November 2020

from vertex import Vertex       # import Vertex class

def load_graph(file):
    file_dictionary = {}        # empty dictionary
    f = open(file, "r")         # opens the file for reading

    # for loop that gets the names and coordinates for vertex objects from the file and adds them to the dictionary
    for line in f:
        new_line = line.strip().split("; ")      # provides the name of the vertex
        name_vertex = new_line[0]
        line_with_coords = new_line[2].split(", ")       # provides the x and y coordinates of the vertex
        vertex = Vertex(name_vertex, line_with_coords[0], line_with_coords[1])
        file_dictionary[vertex.name] = vertex  # adds the data to the dictionary

    f.close()       # closes the file

    f = open(file, "r")     # reopens the file
    # for loop that gets the edges for vertex objects from the file and adds them to the dictionary
    for line in f:
        new_line = line.strip().split("; ")
        name_vertex = new_line[0]
        edges = new_line[1].split(", ")      # provides the edges of the vertex
        # for loop that uses the add_edge method to add the edges for each vertex into the dictionary
        for index in edges:
            file_dictionary[name_vertex].adjacency_list.append(file_dictionary[index])

    f.close()
    return file_dictionary

