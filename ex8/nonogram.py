##############################
# FILE:'ex8'.py
# WRITERS:Yariv_Yarmus
# EXERCISE:intro2cs1 ex8 2021
# DESCRIPTION: nonogram solver
# the standard output(screen).
##############################
from copy import deepcopy


def sum_blocks(lst: list) -> int:
    """
    summarizes the amount of constraints found in lst
    :param lst: a list of constraints
    :return: int: sum
    """
    sum1 = 0
    for i in lst:
        sum1 += i
    return sum1


def constraint_satisfactions(n: int, blocks: list) -> list:
    """
    creates all possible option to fill a row with the constraints in blocks.
    uses helper function.
    :param n:int: length of row.
    :param blocks:list: constraints on row
    :return:list: all the row options
    """
    if len(blocks) == 0:
        return [0] * n
    if n < sum_blocks(blocks):
        return []
    return constraint_satisfactions_helper(blocks, [], [0] * n, 0, 0)


def constraint_satisfactions_helper(blocks: list, lst: list, sub_lst: list, index_sublist: int,
                                    index_blocks: int):
    """
    :param blocks: list. constraints on the row
    :param lst: list. valid row options will be saved to this list
    :param sub_lst: a temporary list for the recursion
    :param index_sublist: keeps track on position inside sub_lst
    :param index_blocks: keeps track on position inside index_blocks
    :return:
    """
    if index_blocks == len(blocks):  # if finished blacks
        lst.append(sub_lst)
        return
    if index_sublist + blocks[index_blocks] > len(sub_lst):  # if out of row
        return
    origin = list(sub_lst)  # make version list
    if not sub_lst[
               max(0, index_sublist - 1)] == 1:  # if the previous not black
        sub_lst[index_sublist:index_sublist + blocks[index_blocks]] = [1] * \
                                                                      blocks[
                                                                          index_blocks]  # change blocks to black
        constraint_satisfactions_helper(blocks, lst, sub_lst,
                                        index_sublist + blocks[index_blocks],
                                        index_blocks + 1)  # recursive call
    constraint_satisfactions_helper(blocks, lst, origin, index_sublist + 1,
                                    index_blocks)  # recursive call - keep white
    return lst


def row_variations(row: list, blocks: list) -> list:
    """
    creates all possible (valid) rows with constraints from blocks.
    :param row:a row/column from the nonogram.
    :param blocks:list of constraints on row
    :return:
    """
    if len(row) < sum_blocks(blocks):
        return [[]]
    return row_variations_helper(blocks, [], row, 0, 0)


def row_variations_helper(blocks: list, lst: list, sub_lst: list, index_sublist: int,
                          index_blocks: int) -> list:
    """
    :param blocks: list. constraints on the row
    :param lst: list. valid row options will be saved to this list
    :param sub_lst: a temporary list for the recursion
    :param index_sublist: keeps track on position inside sub_lst
    :param index_blocks: keeps track on position inside index_blocks
    :return:
    """
    if index_blocks == len(blocks):  # if finished blacks
        if 1 in sub_lst[index_sublist:]:  # there is no other 1 till the end
            # of the row
            return [[]]
        sub_lst[index_sublist:] = [0] * (len(sub_lst) - index_sublist)  # put
        # zeros in the rest of the row
        lst.append(sub_lst)
        return [[]]
    if index_sublist + blocks[index_blocks] > len(sub_lst):  # if out of row
        return [[]]

    origin = list(sub_lst)  # make new version row
    if (not sub_lst[max(0, index_sublist - 1)] == 1 or sub_lst[
        index_sublist] == 1):  # there is space from black (opportunity),
        # or given 1
        if 0 not in sub_lst[
                    index_sublist:index_sublist + blocks[index_blocks]] and \
                (index_sublist + blocks[index_blocks] == len(sub_lst) or
                 sub_lst[index_sublist + blocks[index_blocks]] != 1):  # there
            # are no zeros, and there is no 1 after the block
            sub_lst[index_sublist:index_sublist + blocks[index_blocks]] = [1] * \
                                                                          blocks[
                                                                              index_blocks]
            row_variations_helper(blocks, lst, sub_lst,
                                  index_sublist + blocks[
                                      index_blocks],
                                  index_blocks + 1)
        elif sub_lst[index_sublist] == 1:  # given 1 but not appropriate
            return []
    if origin[index_sublist] != 1:  # if not 1, put 0
        origin[index_sublist] = 0
        row_variations_helper(blocks, lst, origin, index_sublist + 1,
                              index_blocks)

    return lst


def intersection_row(rows: list) -> list:
    """
    receives all possible options for a row and creates a row that crosses all the options.
    :param rows: all the options on a row (row_variation out put or constraint_satisfactions out put)
    :return: a new row
    """
    if len(rows) == 1:
        return rows[0]
    if len(rows) == 0 or len(rows[0]) == 0:
        return []
    new_row = []
    for inside_row in range(len(rows[0])):  # column iteration
        bool1 = True
        for row_num in range(len(rows) - 1):  # rows iteration
            if rows[row_num][inside_row] != rows[row_num + 1][inside_row]:
                bool1 = False
                new_row.append(-1)
                break
        if bool1:
            new_row.append(rows[0][inside_row])
    return new_row


def get_flipped_matrix(orig_matrix: list) -> list:
    """
    receives a nonogram board and "flips" it 90 degrees clockwise.
    :param orig_matrix: games board
    :return: spinned board
    """
    spin_matrix = []
    for column_num in range(len(orig_matrix[0])):
        new_sub_lst = []
        for row_num in range(len(orig_matrix)):
            new_sub_lst.append(orig_matrix[row_num][column_num])
        spin_matrix.append(new_sub_lst)
    return spin_matrix
def dsa()
    nono = 1
    if(nono == 2)


def solve_easy_nonogram(constraints: list) -> list:
    """
    solve a nonogram board with the received constraints using the functions
    up top.
    :param constraints: "rules" on how to fill the board
    :return:
    """
    constraints_rows = constraints[0]
    constraints_cols = constraints[1]
    board = []
    check_dict = {
        1: constraints_cols,
        -1: constraints_rows
    }
    check = -1  # key for check_dict
    first = True
    no_change = [True, 0]  # to follow the no more - changes
    while no_change[1] < 2:  # while not twice no change (col and row)
        no_change[0] = True  # initiate
        if first:  # if first build the options from rows constraints
            for cons in constraints_rows:
                board.append(
                    constraint_satisfactions(len(constraints_cols), cons))
                board[-1] = intersection_row([board[-1]])
            no_change[0] = False
            first = False
        else:  # not the first time
            for index, cons in enumerate(check_dict[check]):  # rows / cols
                origin = list(board[index])  # for check if there was change
                board[index] = row_variations(deepcopy(board[index]),
                                              cons)  # new
                # variations
                board[index] = intersection_row(board[index])  # intersection
                if origin != board[index]:  # there was a change
                    no_change[0] = False
            if no_change[0]:  # not change in this loop
                no_change[1] += 1  # need 2 for rows and cols
            else:
                no_change[1] = 0  # reset
        board = get_flipped_matrix(board)  # spin the matrix (cols<->rows)
        check *= -1  # change constraints row <-> cols

    if check == 1:  # if finished in flipped matrix
        board = get_flipped_matrix(board)
    return board


def finished_board(board: list) -> bool:
    """
    checks if finished building the board
    :param board:
    :return: True if finished
    """
    for row in board:
        if -1 in row:
            return False
    return True


def solve_nonogram(constraints: list) -> list:
    """
    builds all possible boards with the constraints.
    :param constraints:
    :return:list of possible boards
    """
    if not constraints or not constraints[0]:
        return []
    board = solve_easy_nonogram(constraints)  # get conclude board
    if finished_board(board):  # if finished
        return [board]
    return _solve_nonogram_helper(constraints, board,
                                  [])  # backtracking solution


def _solve_nonogram_helper(constraints: list, board: list, boards_lst: list, rows_index=0) -> list:
    """
    helper will create all the possible boards using backtracking
    :param constraints:"rules for filling the nonogram"
    :param board: current game board
    :param boards_lst: saves the possible boards
    :param rows_index: indicates position in board
    :return:
    """
    constraints_rows = constraints[0]
    constraints_cols = constraints[1]

    if rows_index < len(constraints_rows):  # all rows iteration
        # get rows variations
        rows_variations = row_variations(deepcopy(board[rows_index]),
                                         constraints_rows[rows_index])
        if not rows_variations:  # not feet to constrains
            return boards_lst  # stop
        elif len(rows_variations) == 1:  # one solution
            board[rows_index] = rows_variations[0]
        else:  # couple of solutions
            for row in rows_variations:
                board[rows_index] = row
                _solve_nonogram_helper(constraints, deepcopy(board),
                                       boards_lst,
                                       rows_index=rows_index + 1)  # recursive call

    else:
        board = get_flipped_matrix(board)  # spin the matrix (cols<->rows)
        # cols constrains check
        for index, cons in enumerate(constraints_cols):
            rows_variations = row_variations(deepcopy(board[index]), cons)
            if not rows_variations:  # not feet to constrains
                return boards_lst  # stop
            else:
                board[index] = rows_variations[0]
        board = get_flipped_matrix(
            board)  # spin again the matrix (cols<->rows)
        boards_lst.append(board)  # append to list
    return boards_lst  # return the list
print(row_variations([-1, -1, -1], [1, 1]))
print(solve_easy_nonogram([[[2], []], [[1], [1]]]))