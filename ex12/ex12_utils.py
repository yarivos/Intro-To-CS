from boggle_board_randomizer import randomize_board
from typing import Optional, Dict, List, Tuple
import copy
from time import time
import time
# List of constants
BOARD_TYPE = List[List[str]]
SQUARE = Tuple[int]
PATH_TYPE = List[SQUARE]
WORDS_DICT_TYPE = Dict[str, bool]
WORDS_PATH_TYPE = List[Tuple]
MOVING_DIRECTIONS = {'right': (0, 1), 'left': (0, -1), 'down': (1, 0), 'up': (-1, 0),
                     'right_down': (1, 1), 'left_down': (-1, 1), 'right_up': (1, -1), 'left_up': (-1, -1)}


def load_words_dict(file_path: str) -> WORDS_DICT_TYPE:
    """ this function creates a dictionary of words to be used in the game
    file_path: a path to file containing valid words"""
    with open(file_path, 'r') as f:
        words = f.read().splitlines()
        words_dict = {word: True for word in words}
    return words_dict


def is_valid_path(board: BOARD_TYPE, path: PATH_TYPE, words: WORDS_DICT_TYPE) -> Optional[str]:
    """this functions checks if user chose a valid word (checks if word exist in words_dict)
    board: a randomized board as returned by the randomize_board function
    path: a list of tuples e.g. [(3, 1),(3, 2),(2, 1)]  
    words: the dictionary returned from the function load_words_dict
    return: (str) or None. None if path is invalid or word doesnt exist else return the word."""
    if is_path_legal(board, path):
        word = make_current_word(board, path)
        if word in words:  # checks if word is words_dict
            return word


def is_path_legal(board: BOARD_TYPE, path: PATH_TYPE) -> bool:
    """checks if path is legal. all path squares are inside the board and adjacent to each other
    returns True if path is legal else return False"""
    prev = path[0]
    if _is_square_in_board(board, prev):  # check if a path is outside the board
        return False
    list_of_squares = [path[0]]
    for square in path[1:]:
        if square in list_of_squares:  # checks path has the same square twice
            return False
        if _is_square_in_board(board, square):  # check if a path is outside the board
            return False
        if (not -1 <= (prev[0] - square[0])) <= 1 and \
                (not -1 <= (prev[1] - square[1]) <= 1):  # check if squares are adjacent
            return False
        list_of_squares.append(square)
        prev = square
    return True


def _is_square_in_board(board, square) -> bool:
    """ a simple function checks weather or not a square is inside the board """
    return not (0 <= square[0] < len(board)) or not (0 <= square[1] < len(board[0]))


def make_current_word(board: BOARD_TYPE, path: PATH_TYPE) -> str:
    """ This function turns a path into a word, returning it as a string 
        THIS FUNCTION ASSUMES A VALID PATH
        path: a list of tuples e.g. [(3, 1),(3, 2),(2, 1)]  
        board: a randomized board as returned by the randomize_board function """
    #  board[row][column]
    current_word = ''
    for square in path:
        current_letter = board[square[0]][square[1]]
        current_word += current_letter
    return current_word


def find_length_n_words(n, board: BOARD_TYPE, words) -> Optional[WORDS_PATH_TYPE]:
    """function returns all of the words from word_dict which are found in the board."""
    if not (3 <= n <= 16):  # if n isn't legal
        return
    all_words = []
    dict_len_n = _minimize_dic_to_n(words, n)  # filters the dictionary to words with length n
    for row in range(len(board)):  # row iterator
        for column in range(len(board[0])):  # column iterator
            starting_coord = [(row, column)]
            starting_letter = board[row][column]
            _helper_n_length_words(board, dict_len_n, starting_coord, n, starting_letter, all_words)
    return all_words


def _helper_n_length_words(board: BOARD_TYPE, words: dict, path: PATH_TYPE, n: int, pattern: str, all_words_lst: list):
    """
    this function will 'move' in board and insert all the legal words in the board
    into all_words_lst
    """
    if len(path) == n:
        if pattern in words:  # if we found a matching word inside our dict
            if word_not_previously_found(pattern, all_words_lst):  # checks if word was found already
                all_words_lst.append((pattern, path))
        return
    new_dict = _minimize_dic_to_pattern(words, pattern)
    if not new_dict:  # if dict is empty
        return
    lst_of_paths = possible_move_directions(board, path)
    for new_path in lst_of_paths:
        new_letter = last_letter(board, new_path[-1])  # returns the last letter in path
        _helper_n_length_words(board, new_dict, new_path, n, pattern + new_letter, all_words_lst)


def word_not_previously_found(word, lst_of_words):
    """checks if word is inside lst_of_words"""
    for words in lst_of_words:
        if word in words:
            return False
    return True


def possible_next_squares(square: tuple) -> List[tuple]:
    """
    function will create all the possible moves from a square
    this function doesn't check if a square is legal
    """
    list_pos_squares = []
    for direction in MOVING_DIRECTIONS:
        list_pos_squares.append(
            (square[0] - MOVING_DIRECTIONS[direction][0], square[1] + MOVING_DIRECTIONS[direction][1]))
    return list_pos_squares


def last_letter(board: BOARD_TYPE, coordinate: tuple) -> str:
    """returns a letter in board"""
    letter = board[coordinate[0]][coordinate[1]]
    return letter


def possible_move_directions(board: BOARD_TYPE, path) -> List[PATH_TYPE]:
    """function returns all the next legal moves from the last square"""
    legal_paths = []
    possible_next_square = possible_next_squares(path[-1])
    for square in possible_next_square:
        path.append(square)
        if is_path_legal(board, path):
            legal_paths.append(copy.copy(path))
        path.pop()
    return legal_paths


def _minimize_dic_to_n(words_dict: WORDS_DICT_TYPE, n: int) -> WORDS_DICT_TYPE:
    """function will return a smaller dictionary which contains only words on len(n)
    words_dict:(Dict). 
    n: (Int). length of words"""
    minimized_word_dict = {}
    for key in words_dict:  # iterates over all of the keys in dictionary
        if len(key) != n:  # checks if key is equal to word length (n)
            continue
        minimized_word_dict[key] = True
    return minimized_word_dict


def _minimize_dic_to_pattern(words_dict: WORDS_DICT_TYPE, pattern) -> WORDS_DICT_TYPE:
    """function will return a smaller dictionary which contains possible words
    which are a continuation of curr_pattern
    curr_pattern: (Str). pattern of letters.
    curr_dict:(Dict). dictionary of words"""
    minimized_word_dict = {}
    for key in words_dict:  # iterates over all of the keys in dictionary
        if key.startswith(pattern):
            minimized_word_dict[key] = True
    return minimized_word_dict


