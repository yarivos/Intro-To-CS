##############################
# FILE:'wordsearch'.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex5 2021
# DESRIPTION: word searching algorithm
# the standard output(screen).
##############################
import copy
import sys


def read_wordlist(filename):
    """
    builds a list of possible words from file
    :param filename: path to words file
    :return: list of the possible words
    """
    word_lst = []
    words_file = open(filename, 'r')
    for word in words_file:
        word_lst.append(word[:len(word) - 1:])
    return word_lst


def read_matrix(filename):
    """
    building a matrix from a file.
    :param filename: path to the file.
    :return: a list of lists, the matrix
    """
    letters_from_file = open(filename, 'r')
    letters_matrix = []
    for row in letters_from_file:
        row_list = []
        for letter in row:
            if letter != ',' and letter != '\n':
                row_list.append(letter)
        letters_matrix.append(row_list)
    return letters_matrix


def find_words(word_list, matrix, directions):
    """
    function receives words to check in the matrix in the directions chosen.
    :param word_list: type: list[]. all optional words to check in the matrix
    :param matrix: typle: list[list].
    :param directions: type: string. chosen direction to check for words
    :return: A list of tuples which state the words found and the amount.
    """
    amounts_lst = []
    if len(matrix) == 0:
        return amounts_lst
    for direct in directions:
        if direct == 'u' or direct == 'd':
            direction_up_down_or_left_right(word_list, get_spinned_matrix(matrix), direct, amounts_lst)

        if direct == 'r' or direct == 'l':
            direction_up_down_or_left_right(word_list, matrix, direct, amounts_lst)

        if direct == 'w' or direct == 'z':
            direction_up_right_down_left(word_list, matrix, direct, amounts_lst)

        if direct == 'x' or direct == 'y':
            direction_up_right_down_left(word_list, get_spinned_matrix(matrix), direct, amounts_lst)
    return get_words_to_tuple(amounts_lst)


def direction_up_down_or_left_right(word_list, matrix, direction, amounts_lst):
    """
    function checks for words from words list in the matrix by the direction chosen.
    :param word_list: type: list[]. all optional words to check in the matrix
    :param matrix: typle: list[list].
    :param direction: type: string. chosen direction to check for words. possible parameters: u, d, l, r
    :param amounts_lst: type: list[list]. all the current words found the amount
    :return:
    """
    for row in matrix:
        row_string = "".join(row)
        if direction == 'u' or direction == 'r':
            count_words(word_list, row_string, amounts_lst)
        else:
            count_words(word_list, row_string[::-1], amounts_lst)


def direction_up_right_down_left(word_list, matrix, direction, amounts_lst):
    """
    This function will check the diagonals for words from wordlist, and insert them into amounts_lst
    :param word_list: type: list[]. all optional words to check in the matrix
    :param matrix: typle: list[list].
    :param direction: type: string. chosen direction to check for words. possible parameters: x, z, y, w
    :param amounts_lst: type: list[list]. all the current words found the amount
    :return: None
    """
    counter_row = 0
    counter_column = 1
    while True:
        letter_lst = []
        if counter_row != len(matrix):
            for col in range(counter_row + 1):
                try:
                    letter_lst.append(matrix[counter_row - col][col])
                except:
                    break
        else:
            for col in range(0, len(matrix)):
                try:
                    letter_lst.append(matrix[counter_row - 1 - col][counter_column + col])
                except:
                    break
        if counter_row != len(matrix):
            counter_row += 1
        else:
            counter_column += 1

        letter_str = ''.join(letter_lst)
        if direction == 'w' or direction == 'x':
            count_words(word_list, letter_str, amounts_lst)
        else:
            count_words(word_list, letter_str[::-1], amounts_lst)
        if (counter_row == len(matrix)) and (counter_column == len(matrix[0])):
            return


def get_words_to_tuple(amount_lst):
    """
    function receives all the words and their amount found in the matrix and
    transfer the values into a new list of tuples of this values.
    :param amount_lst: type: list[list], all the words found in the matrix
    :return: new list of tuples with words and amount found.
    """
    new_words_list = []
    for i in range(len(amount_lst)):
        words_tuple = amount_lst[i][0], amount_lst[i][1]
        new_words_list.append(words_tuple)
    return new_words_list


def count_words(word_list, check_string, amounts_lst):
    """
    the function gets a string from the matrix by the chosen direction and checks if there
    are matching words from the word list inside it.
    :param amounts_lst: all the words found in the matrix
    :param word_list: type: list. all the words which are needed to be found in the string
    :param check_string: type: string. a string of letters from the matrix, assimilated by the chosen direction
    :return: None
    """
    for word in word_list:
        check_from = 0
        word_counter = 0
        while check_from < len(check_string):
            str_position = check_string.find(word, check_from)
            if str_position != -1:
                word_counter += 1
                check_from = str_position + 1
            else:
                break
        if word_counter != 0:
            add_word_amount(word, word_counter, amounts_lst)


def add_word_amount(word, amount, amounts_lst):
    """
    adds the amount of occurrences of a word in the matrix found by the direction chosen to a list.
    if the word is already inside, it updates it amount in the list or it adds the word.
    :param amounts_lst: all the words found in the matrix
    :param word: type: string.  all the words that needs to be checked in the matrix(by the chosen direction
    :param amount: type: int. how many times the word was found.
    :return: None.
    """
    for i in range(len(amounts_lst)):
        if amounts_lst[i][0] == word:
            amounts_lst[i][1] += amount
            return
    amounts_lst.append([word, amount])
    return


def get_spinned_matrix(orig_matrix):
    """
    function spins the matrix 90 degrees clockwise
    :param orig_matrix: type:list[list]
    :return:  a spinned matrix.
    """
    copied_matrix = copy.deepcopy(orig_matrix)
    spin_matrix = []
    for column_num in range(len(orig_matrix[0])):
        new_sub_lst = []
        for row_num in range(len(orig_matrix) - 1, -1, -1):
            new_sub_lst.append(copied_matrix[row_num][column_num])
        spin_matrix.append(new_sub_lst)
    return spin_matrix


def write_output(results, filename):
    """
    function takes the results found and puts them in a file.
    :param results: type: list[tuple]. all the words found in the matrix and the amount
    :param filename: name of the new created file of the result
    :return: None
    """
    out_put_file = open(filename, 'w+')
    for line in results:
        out_put_file.write(line[0] + ',')
        out_put_file.write(str(line[1]))
        out_put_file.write("\n")
    out_put_file.close()


def main(word_file, matrix_file, output_file, directions):
    """
    uses other functions
    :param word_file: path to word file
    :param matrix_file: path to matrix file
    :param output_file: name of created result file
    :param directions: string of directions to check for words
    :return: None
    """
    words_list = read_wordlist(word_file)
    matrix = read_matrix(matrix_file)
    found_words_lst = find_words(words_list, matrix, directions)
    write_output(found_words_lst, output_file)


def check_matrix_path():
    """
    check if matrix file path is valid
    :return: None
    """
    try:
        open(sys.argv[2])
    except IOError:
        print('matrix file does not exist in the desired location')
        sys.exit()


def check_words_path():
    """
    checks if words file path is valid
    :return: None
    """
    try:
        open(sys.argv[1])
    except IOError:
        print('words file does not exist in the desired location')
        sys.exit()


def check_parameter_len():
    """
    check if number of arguments received to the algorithm is valid
    :return: None
    """
    if len(sys.argv) != 5:
        print('You have entered a wrong number of parameters.\n'
              'The algorithm needs 4 parameters in the following order:\n'
              '1)name of words file\n'
              '2)name of matrix file\n'
              '3)name for output file\n'
              '4)directions for words in matrix')
        sys.exit()


def check_directions():
    """
    checks if the directions received are valid
    :return: None
    """
    for letter in sys.argv[4]:
        if not (letter in 'udrlwxyz'):
            print('you have a entered an invalid direction:\n'
                  'valid directions are:\n'
                  '1) up - "u"\n'
                  '2) down - "d"\n'
                  '3) left - "l"\n'
                  '4) right - "r"\n'
                  '5) right, up - "w"\n'
                  '6) right, down - "y"\n'
                  '7) left, up - "x"\n'
                  '8) left, down - "z"\n')
            sys.exit()


def check_parameters():
    check_parameter_len()
    check_words_path()
    check_matrix_path()
    check_directions()


if __name__ == "__main__":
    check_parameters()
    main(*sys.argv[1:])