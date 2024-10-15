from typing import List
import sys
BOARD_LENGTH = 7
VERTICAL = 0
HORIZONTAL = 1
LEGAL_NAMES = "YBOGWR"

class Board:
    """
    Board manages all the display of the game and most validates the coordination
    between the object cars.
    """
    __board: List[List[str]]

    def __init__(self):
        self.__board = [["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"],
                        ["_", "_", "_", "_", "_", "_", "_"]]
        self.__cars = []

    def __str__(self):
        """
        This function is called when find_me board object is to be printed.
        :return: A string of the current status of the board
        """
        return str(self.__board)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        coordinates_lst = []
        for i in range(len(self.__board)):
            for j in range(len(self.__board[0])):
                coordinates_lst.append((i, j))
                if i == 3 and j == 6:
                    coordinates_lst.append((3, 7))
        return coordinates_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        moves_lst = []
        for car in self.__cars:
            car_name = car.get_name()
            car_moves = []
            if "u" in car.possible_moves():
                if self.in_board(car.movement_requirements("u")) and not self.cell_content(car.movement_requirements("u")):
                    car_moves.append(car_name + ", car can move up by clicking ""u")
                if self.in_board(car.movement_requirements("d")) and not self.cell_content(car.movement_requirements("d")):
                    car_moves.append(car_name + ", car can move down by clicking ""d")
            if "l" in car.possible_moves():
                if self.in_board(car.movement_requirements("l")) and not self.cell_content(car.movement_requirements("l")):
                    car_moves.append(car_name + ", car can move left by clicking ""l")
                if self.in_board(car.movement_requirements("r")) and not self.cell_content(car.movement_requirements("r")):
                    car_moves.append(car_name + ", car can move right by clicking ""r")
            moves_lst.append(car_moves)
        return moves_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if not self.in_board(coordinate):
            return
        if self.__board[coordinate[0]][coordinate[1]] == "_":  # if coordinates empty
            return None
        return self.__board[coordinate[0]][coordinate[1]]  # name of car in coordinates

    def add_car(self, car):
        """
        Adds find_me car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        if self.is_legal_car(car):  # checks if car is legal
            return False
        locations = car.car_coordinates()
        for j in locations:  # placing the car on the board
            self.__board[j[0]][j[1]] = car.get_name()
        self.__cars.append(car)
        return True  # if car is valid

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if movekey not in "udlr" or len(movekey) != 1:  # if movekey is not legal direction
            return False  ###### might need to print
        car_to_move = None
        for curr_car in self.__cars:  # finds the car object with arg name
            if name == curr_car.get_name():
                car_to_move = curr_car
                break
        if not car_to_move:  # if car name doesn't exist
            return False
        car_coord_lst = car_to_move.car_coordinates()
        moving_location = car_to_move.movement_requirements(movekey)  # location to move to
        if moving_location[0] == 3 and moving_location[1] == 7:
            print("You have Won")
            sys.exit()
        if not (0 <= moving_location[0] <= 6) or not (
                0 <= moving_location[1] <= 6):  # checks if moving location is inside the board
            return False

        if not self.in_board(moving_location) or self.__board[moving_location[0]][moving_location[1]] != "_":  # checks if empty location
            return False
        if not car_to_move.move(movekey):  # tries to move the car
            return False
        self.erase_car_trace(car_coord_lst, movekey)  # changes moved from location on board to "_"
        self.__board[moving_location[0]][moving_location[1]] \
            = car_to_move.get_name()  # puts car's name in the new location
        return True

    def erase_car_trace(self, car_coord_lst, movekey):
        """
        erases the car traces after each move
        :param car_coord_lst:
        :param movekey:
        :return:
        """
        if movekey == "u":
            self.__board[car_coord_lst[-1][0]][car_coord_lst[-1][1]] = "_"
        if movekey == "d":
            self.__board[car_coord_lst[0][0]][car_coord_lst[0][1]] = "_"
        if movekey == "r":
            self.__board[car_coord_lst[0][0]][car_coord_lst[0][1]] = "_"
        if movekey == "l":
            self.__board[car_coord_lst[-1][0]][car_coord_lst[-1][1]] = "_"

    def is_legal_location(self, car):
        """
        checks if the location is legal to put the car inside
        :param car:
        :return:
        """
        locations = car.car_coordinates()
        if not 2 <= len(locations) <= 4:
            return True
        for cur_location in locations:
            if cur_location[0] == 3 and cur_location[1] == 7:
                print("You Have Won")
                sys.exit()
            if not (0 <= cur_location[0] < BOARD_LENGTH) or not (0 <= cur_location[1] < BOARD_LENGTH):  # if find_me location is out of the board
                return True
        for i in locations:  # all coordinates of the car
            if self.cell_content(i) is not None:  # if coordinates has find_me car in them
                return True

    def in_board(self, coords):
        """
        checks if the location is inside the board
        :param coords: location of sort (row,col)
        :return:
        """
        if (coords[0] == 3 and coords[1] == 7) or (0 <= coords[0] <= 6 and 0 <= coords[1] <= 6):
            return True

    def is_legal_car(self, car):  # uses all legal functions
        if self.is_legal_location(car):
            return True
