# Alina Chadwick
# CS1 Prof. Balckom
# Lab 3 - City class
# October/November 2020

# functions that sort the cities based on name, latitude, and population

from quicksort import sort
from world_cities import list_of_cities, text_output

# uses instance variable "city_latitude" to compare the latitudes of two cities
def compare_latitudes(a, b):
    return a.city_latitude <= b.city_latitude

# uses instance variable "city_name" to compare the names of two cities alphabetically,
# uses function lower to make the strings lowercase
def compare_names(a, b):
    return a.city_name.lower() <= b.city_name.lower()

# uses instance variable "city_population" to compare the populations of two cities,
# in order to sort from highest population to lowest, the return value is if b<=a rather than if a<=b
def compare_populations(a, b):
    return b.city_population <= a.city_population

def compare(compare_func, x, y):        # general compare function in which other compare functions can be used
    return compare_func(x, y)

def sort_cities_name():     # sorts by name, alphabetically
    sort(list_of_cities, compare_names)
    text_output(list_of_cities, "cities_alpha.txt")     # outputs into output file "cities_alpha.txt"

def sort_cities_population():       # sorts by population, high to low
    sort(list_of_cities, compare_populations)
    text_output(list_of_cities, "cities_pop.txt")   # outputs into output file "cities_pop.txt"

def sort_cities_latitude():     # sorts by latitude values, low to high
    sort(list_of_cities, compare_latitudes)
    text_output(list_of_cities, "cities_latitude.txt")  # outputs into output file "cities_latitude.txt"

sort_cities_name()
sort_cities_population()
sort_cities_latitude()