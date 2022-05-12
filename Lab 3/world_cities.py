# Alina Chadwick
# CS1 Prof. Balckom
# Lab 3 - City class
# October/November 2020

# Uses the City class to create a file with city objects

from city import City

text_file = open("world_cities.txt", "r")       # opens original file for reading
list_of_cities = []     # blank list

# for loop that appends the blank list with values from each city object
for line in text_file:
    new_line = line.strip().split(",")      # strips the line of whitespace and splits it into list indices
    city_object = City(new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], new_line[5])        # uses list indices to create a city object
    list_of_cities.append(city_object)      # appends the city object to the list

text_file.close()       # closes the file

def text_output(list, file):
    text_file = open(file, "w")     # creates a new text file to insert the new lines into

    # for loop that takes cities from the list of cities and adds the information into the new text file
    for city in list:
        text_file.write(str(city) + "\n")       # "\n" allows for the cities to be on different lines

    text_file.close()       #closes the file

text_output(list_of_cities, "cities_out.txt")