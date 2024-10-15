import math


class Asteroid:
    """This is the asteroid class. contains all the methods and properties 
    to create functioning asteroids"""

    def __init__(self, speed_x, location_x, speed_y, location_y, size):
        """this the constructor method for the asteroid. it initiates an asteroid instance with
        default values"""
        self.__speed_x = speed_x
        self.__location_x = location_x
        self.__speed_y = speed_y
        self.__location_y = location_y
        self.__size = size

    def get_speed_x(self):
        """a method used to get the asteroid's x-axis speed
        returns: the asteroid's speed to the x axis"""
        return self.__speed_x

    def get_speed_y(self):
        """a method used to get the asteroid's y-axis speed
        returns: the asteroid's speed to the y axis"""
        return self.__speed_y

    def get_location_x(self):
        """a method used to get the asteroid's location on the x-axis"""
        return self.__location_x

    def get_location_y(self):
        """a method used to get the asteroid's location on the y-axis"""
        return self.__location_y

    def get_size(self):
        """a method used to get the asteroid's size"""
        return self.__size

    def set_speed_x(self, speed):
        """a method used to set the asteroid's speed on the x-axis"""
        self.__speed_x = speed
        return

    def set_speed_y(self, speed):
        """a method used to set the asteroid's speed on the y-axis"""
        self.__speed_y = speed
        return

    def set_location_x(self, location):
        """a method used to set the asteroid's location on the x-axis"""
        self.__location_x = location
        return

    def set_location_y(self, location):
        """a method used to set the asteroid's location on the y-axis"""
        self.__location_y = location
        return

    def has_intersection(self, obj):
        """
        checks if there is a collision with the asteroid
        """
        distance = math.sqrt((obj.get_location_x() - self.__location_x) ** 2 +
                             (obj.get_location_y() - self.__location_y) ** 2)
        if distance <= ((self.__size * 10) - 5) + obj.get_radius():
            return True
        return False
