from ex12_utils import *

words1 = {'DOG': True, 'DFH': True, 'DAT': True}
my_board1 = [['D','O','G'],['F', 'A', 'T'],['H', 'O', 'T']]
legal_path_row = [(0,0), (0,1), (0,2)]
legal_path_col = [(0,0), (1,0), (2,0)]
legal_path_diag = [(0,0), (1,1), (2,2)]
path_outside1 = [(-1,0), (0,0), (0,1)]
path_not_adjacent1 = [(0,0), (1,2)]
path_same_square = [(0,0),(1,1),(0,1),(0,0)]

def test_make_current_word():
    assert make_current_word(my_board1, legal_path_row) == 'DOG'
    assert make_current_word(my_board1, legal_path_col) == 'DFH'
    assert make_current_word(my_board1, legal_path_diag) == 'DAT'

def test_is_path_legal():
    assert is_path_legal(my_board1, legal_path_row) == True
    assert is_path_legal(my_board1, legal_path_col) == True
    assert is_path_legal(my_board1, legal_path_diag) == True
    assert is_path_legal(my_board1, path_outside1) == False
    assert is_path_legal(my_board1, path_not_adjacent1) == False
    assert is_path_legal(my_board1, path_same_square) == False


def test_is_valid_path1():
    assert is_valid_path(board = my_board1, path = legal_path_row, words=words1) == 'DOG'


print(possible_next_squares((1,1)))
#  [(1, 2), (1, 0), (0, 1), (2, 1), (0, 2), (2, 2), (2, 2), (2, 0)]
