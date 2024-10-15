POSSIBLE_MOVES_LIST = [{"u": "cause the car to go up.\n",
                         "d": "cause the car to go down."},
                       {"l": "cause the car to go left.\n",
                         "r": "cause the car to go right."}]
LEGAL_NAMES = "YBOGWR"
VERTICAL = 0
HORIZONTAL = 1


class Car:
    """
    holds all information for car object
    mostly communicates with board to allow moves and change the car attributes

    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for find_me Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        return self._car_coordinates_helper()

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        x = POSSIBLE_MOVES_LIST[self.__orientation]
        return x

    def movement_requirements(self, movekey):  ############################## might need to check legal movekey
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        car_coord = self.car_coordinates()
        if movekey == "u":
            return [self.__location[0] - 1, self.__location[1]]
        elif movekey == "d":
            return [car_coord[-1][0] + 1, car_coord[-1][1]]
        elif movekey == "l":
            return [self.__location[0], self.__location[1] - 1]
        elif movekey == "r":
            return [car_coord[-1][0], car_coord[-1][1] + 1]

    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if not self.check_orientation(movekey):  # checks if moving direction is legal for car orientation
            return False
        self.set_location(movekey)
        return True

    def set_location(self, movekey):
        """
        sets car new location after each move
        :param movekey:
        :return:
        """
        if movekey == "u":
            self.__location = (self.__location[0] - 1, self.__location[1])
        if movekey == "d":
            self.__location = (self.__location[0] + 1, self.__location[1])
        if movekey == "l":
            self.__location = (self.__location[0], self.__location[1] - 1)
        if movekey == "r":
            self.__location = (self.__location[0], self.__location[1] + 1)

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name

    def _car_coordinates_helper(self):
        """
        helper for car_coordinates
        :return: all of the car's coordinates
        """
        coordinates_lst = []
        for i in range(self.__length):
            if self.__orientation == 1:  # if orientation = Horizontal
                coordinates_lst.append((self.__location[0], self.__location[1] + i))
            else:  # if orientation = Vertical
                coordinates_lst.append((self.__location[0] + i, self.__location[1]))
        return coordinates_lst

    def check_orientation(self, movekey):
        """
        checks if the orientation given is legal with cars movekey
        :param movekey:
        :return:
        """
        if self.__orientation == VERTICAL:
            if movekey not in "ud":
                return False
        if self.__orientation == HORIZONTAL:
            if movekey not in "lr":
                return False
        return True


