##############################
# FILE:'ex9'.py
# WRITERS:Yariv_Yarmus
# EXERCISE:intro2cs1 ex9 2021
# DESRIPTION: rush hour game
# the standard output(screen).
##############################
import sys
from board import *
from car import *
import helper

LEGAL_NAMES = "YBOGWR"
LEGAL_ORIENTATION = [0, 1]
LEGAL_LENGTH = 7
LEGAL_DIR = ["l", "u", "d", "r"]


class Game:
    """
    game manages each turn of the game and the prints.
    """

    def __init__(self, board):
        """
        Initialize find_me new Game object.
        :param board: An object of type board
        """
        self.__game = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of find_me turn, you may print additional
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        print(self.__game)
        print(self.__game.possible_moves())
        user_input = input("Hello, choose a name of car to move and direction.\n"
                           "if you want to finish click""!")
        try:
            car_to_move, move_dir = user_input.split(",")
        except ValueError:
            return
        if car_to_move not in LEGAL_NAMES or move_dir not in LEGAL_DIR:
            print("illegal inputs, legal names are - " + LEGAL_NAMES + "\n"
                                                                       "legal directions are 0 for Vertical 1 for Horizontal")
            return
        if user_input == "!":
            print("GoodBye")
            sys.exit()
        if self.__game.move_car(car_to_move, move_dir):
            return True
        print("invalid try")

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while True:
            if not self.__single_turn():
                continue
            if self.__game.cell_content(self.__game.target_location()):
                print(self.__game)
                print("You Have Won!")
                sys.exit()


if __name__ == "__main__":
    def check_range(num):
        """
        check if num in range
        :param num:
        :return:
        """
        if 6 >= num >= 0:
            return True

    def is_winning(len1, loc):
        if loc[0] == 3 and ((loc[1] + len1) >= 7):
            print("You Won")
            sys.exit()
        return True

    def check_car(file_json, json_key):
        """
        checks if a car is legal before adding it to board
        """
        if json_key in LEGAL_NAMES and len(json_key) == 1:  # legal name
            if 2 <= file_json[json_key][0] <= 4:  # legal length
                if check_range(file_json[json_key][1][0]) and check_range(file_json[json_key][1][1]):  # legal location
                    if file_json[json_key][2] == 0 or file_json[json_key][2] == 1:  # legal orientation
                        if is_winning(file_json[json_key][0], file_json[json_key][1]):
                            if check_len_loc(file_json[json_key][0], file_json[json_key][1]):
                                return True

    def check_len_loc(len, loc):
        if len + loc[0] > 6 or len + loc[1] > 6:
            return False
        return True

    file_json = helper.load_json(sys.argv[1])
    game_board = Board()
    for json_key in file_json:
        if check_car(file_json, json_key):
            car_name = json_key
            car_length = file_json[json_key][0]
            car_location = file_json[json_key][1]
            car_orientation = file_json[json_key][2]
            curr_car = Car(car_name, car_length, car_location, car_orientation)
            game_board.add_car(curr_car)
    play_game = Game(game_board)
    play_game.play()
