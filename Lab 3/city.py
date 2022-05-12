# Alina Chadwick
# CS1 Prof. Balckom
# Lab 3 - City class
# October/November 2020
# Develop a class of city objects that describe a city's name, country code, region, population, latitude, and longitude

class City:
    # initial values for each city object
    def __init__(self, country_code, city_name, city_region, city_population, city_latitude, city_longitude):
        self.country_code = str(country_code)       # two letter country code
        self.city_name = str(city_name)     # name of the city
        self.city_region = str(city_region)     # the region in which the city is located
        self.city_population = int(city_population)      # the population of the city
        self.city_latitude = float(city_latitude)      # the city's latitude coordinates
        self.city_longitude = float(city_longitude)       # the city's longitude coordinates

    # returns the values of the city's name, population, latitude, and longitude in a string
    def __str__(self):
        return str(self.city_name) + "," + str(self.city_population) + "," + str(self.city_latitude) + "," + str(self.city_longitude)

