from typing import SupportsAbs
import math

# Constants
LIFE_TIME_TORPEDO = 200
TORPEDO_RADIUS = 4


class Torpedo:
    """This is the torpedo class. contains all the methods and properties 
    to create functioning torpedos"""

    def __init__(self, speed_x=0, speed_y=0, location_x=None, location_y=None, heading=0):
        """this the constructor method for the torpedo. it initiates a torpedo instance with
        default values"""
        self.__speed_x = speed_x + 2 * math.cos(math.radians(heading))
        self.__speed_y = speed_y + 2 * math.sin(math.radians(heading))
        self.__location_x = location_x
        self.__location_y = location_y
        self.__heading = heading
        self.__radius = TORPEDO_RADIUS
        self.__life_time = LIFE_TIME_TORPEDO

    def get_speed_x(self):
        """a method used to get the torpedo's x-axis speed
        returns: the torpedo's speed to the x axis"""
        return self.__speed_x

    def get_speed_y(self):
        """a method used to get the torpedo's y-axis speed
        returns: the torpedo's speed to the y axis"""
        return self.__speed_y

    def get_location_x(self):
        """a method used to get the torpedo's location on the x-axis"""
        return self.__location_x

    def get_location_y(self):
        """a method used to get the torpedo's location on the y-axis"""
        return self.__location_y

    def get_radius(self):
        """a method used to get the torpedo's radius"""
        return self.__radius

    def set_location_x(self, location):
        """a method used to set the torpedo's location on the x-axis"""
        self.__location_x = location
        return

    def set_location_y(self, location):
        """a method used to set the torpedo's location on the y-axis"""
        self.__location_y = location
        return

    def get_heading(self):
        """a method used to get the torpedo's heading"""
        return self.__heading

    def get_life_time(self):
        """ a method used to get the life time of the torpedo """
        return self.__life_time

    def reduce_life_time(self):
        """a method used to reduce torpedo's life time by 1"""
        self.__life_time -= 1
