##############################
# FILE:'ex7'.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex7 2021
# DESRIPTION: practice use of recursion
# the standard output(screen).
##############################


OPEN = '('
CLOSE = ')'


def print_to_n(n: int) -> None:
    """
    print all the numbers until the n number
    :param n:
    :return:
    """
    if n <= 0:
        return
    print_to_n(n - 1)
    print(n)


def digit_sum(n: int) -> int:
    """
    return the sum of the digits of n
    :param n:
    :return:int. sum
    """
    if n <= 0:
        return 0
    return n % 10 + digit_sum(n // 10)


def is_prime(n: int) -> bool:
    """
    checks if n is a prime number
    :param n:
    :return:
    """
    if n <= 1:
        return False
    x = []
    _has_divisor_smaller_than(n, 2, x)
    return x[0]


def _has_divisor_smaller_than(n: int, i: int, x: list):
    """
    checks if n has a smaller divisor
    :param n:
    :param i:
    :param x:
    :return:
    """
    if n == i:
        x.append(True)
        return
    if n % i == 0:
        x.append(False)
        return
    _has_divisor_smaller_than(n, i + 1, x)


def play_hanoi(hanoi, n, src, dst, temp):
    """
    solves tower of hanoi game
    :param hanoi:
    :param n:
    :param src:
    :param dst:
    :param temp:
    :return:
    """
    if n <= 0:
        return
    play_hanoi(hanoi, n - 1, src, temp, dst)
    hanoi.move(src, dst)
    play_hanoi(hanoi, n - 1, temp, dst, src)


def print_sequences(char_list: list, n: int) -> None:
    """
    print all possible permutations from char_list
    :param char_list:list of characters
    :param n:int. length of permutations
    :return:
    """
    _print_sequences_helper(char_list, n, "")


def _print_sequences_helper(char_list: list, n: int, seq: str) -> None:
    """
    :param char_list:
    :param n:
    :param seq: builds all the sequences(permutations)
    :return:
    """
    if len(seq) == n:
        print(seq)
        return
    for i in char_list:
        _print_sequences_helper(char_list, n, seq + i)


def print_no_repetition_sequences(char_list: list, n: int) -> None:
    """
    print all possible permutations with out repetitions of cases
    :param char_list:list of characters
    :param n:int. length of permutations
    :return:
    """
    if len(char_list) < n:
        return
    _print_no_sequences_helper(char_list, n, "")


def _print_no_sequences_helper(char_list: list, n: int, seq: str) -> None:
    """
    :param seq: builds all the sequences(permutations)
    """
    if len(seq) == n:
        print(str(seq))
        return
    for i, char in enumerate(char_list):
        _print_no_sequences_helper(char_list[:i] + char_list[i + 1:], n, seq + char)


def parentheses(n: int) -> list:
    """
    prints all possible options of n brackets.
    :param n:int. amount of brackets
    :return:list with all possible ways to put brackets.
    """
    lst = []
    par_helper(n, 0, 0, lst, '')
    return lst


def par_helper(n: int, opened: int, closed: int, lst: list, sub: str):
    """
    :param n:
    :param opened: number of opened brackets
    :param closed: number of closed brackets
    :param lst:
    :param sub:builds the ways to put brackets
    :return:
    """
    if len(sub) == 2 * n:
        lst.append(sub)
        return
    if opened <= closed:
        par_helper(n, opened + 1, closed, lst, sub + OPEN)
    else:
        if opened < n:
            par_helper(n, opened + 1, closed, lst, sub + OPEN)
        if closed < n:
            par_helper(n, opened, closed + 1, lst, sub + CLOSE)


def flood_fill(image: list, start: tuple) -> None:
    """
    changes the sequences of dots into *
    :param image:a list of lists (array), filled with "." and "*"
    :param start:tuple. indicates the starting point in the array.
    :return:
    """
    if image[start[0]][start[1]] == "*":
        return
    image[start[0]][start[1]] = "*"
    flood_fill(image, (start[0] + 1, start[1]))
    flood_fill(image, (start[0], start[1] + 1))
    flood_fill(image, (start[0], start[1] - 1))
    flood_fill(image, (start[0] - 1, start[1]))





















