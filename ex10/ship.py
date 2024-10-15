from typing import SupportsAbs
import math


class Ship:
    """This is the ship class. It has all the methods and properties needed to have a working ship."""

    def __init__(self, speed_x=0, speed_y=0, location_x=None, location_y=None, heading=0):
        """the constructor method for the ship. creates a ship with default values"""
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__location_x = location_x
        self.__location_y = location_y
        self.__heading = heading
        self.__radius = 1
        self.__lives = 3

    def get_speed_x(self):
        """a method used to get the ship's x-axis speed
        returns: the ship's speed to the x axis"""
        return self.__speed_x

    def get_speed_y(self):
        """a method used to get the ship's y-axis speed
        returns: the ship's speed to the y axis"""
        return self.__speed_y

    def get_location_x(self):
        """a method used to get the ship's location on the x-axis"""
        return self.__location_x

    def get_location_y(self):
        """a method used to get the ship's location on the y-axis"""
        return self.__location_y

    def get_radius(self):
        """a method used to get the ship's radius"""
        return self.__radius

    def set_speed_x(self, speed):
        """a method used to set the ship's x-axis speed"""
        self.__speed_x = speed
        return

    def set_speed_y(self, speed):
        """a method used to set the ship's y-axis speed"""
        self.__speed_y = speed
        return

    def set_location_x(self, location):
        """a method used to set the ship's location on the x-axis"""
        self.__location_x = location
        return

    def set_location_y(self, location):
        """a method used to set the ship's location on the y-axis"""
        self.__location_y = location
        return

    def set_heading(self, new_heading):
        """a method used to set the ship's heading"""
        self.__heading += new_heading

    def get_heading(self):
        """a method used to get the ship's heading"""
        return self.__heading

    def get_life(self):
        """a method used to get the amounts of lives"""
        return self.__lives

    def reduce_life(self):
        """a method used to reduce ship's life by 1"""
        self.__lives -= 1
