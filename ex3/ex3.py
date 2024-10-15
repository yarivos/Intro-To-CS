##############################
# FILE:ex3.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex2 2021
# DESRIPTION: a vary of Functions using list and loops
# the standard output(screen).
##############################

# this function returns a list of numbers user inputs with the sum
def input_list():
    lst_num = []
    num_sum = 0
    while True:  # continues until user enters an empty string
        user_input = input()
        if user_input != '':
            user_input = float(user_input)
            lst_num.append(user_input)
            num_sum += user_input
            continue
        else:
            lst_num.append(num_sum)
            return lst_num


# the function returns an inner product of two vectors
def inner_product(vec_1, vec_2):
    if len(vec_1) != len(vec_2):  # checks the length of the vectors
        return
    vec_product = 0
    for i in range(len(vec_1)):  # runs through all objects inside the list
        vec_product += float(vec_1[i]) * float(vec_2[i])
    return vec_product


# receives a list of numbers and check if values are sorted from small to big
# or other way around or equal
def sequence_monotonicity(sequence):
    lst_check = [True, True, True, True]
    for i in range(len(sequence) - 1):  # runs through all objects in sequence
        if not (sequence[i] <= sequence[i + 1]):
            lst_check[0] = False
        if not (sequence[i] < sequence[i + 1]):
            lst_check[1] = False
        if not (sequence[i] >= sequence[i + 1]):
            lst_check[2] = False
        if not (sequence[i] > sequence[i + 1]):
            lst_check[3] = False
    print(lst_check)


# function receives a list of boolean values and return an example of a list
# with numbers that fit the description.
def monotonicity_inverse(def_bool):
    # this next lines set up specific options of values which can be received
    if def_bool.count(True) >= 3 or def_bool.count(False) > 3:
        return None

    if def_bool[0] and def_bool[2]:
        return [1, 1, 1, 1]

    if def_bool[0]:
        if def_bool[3]:
            return
        if def_bool[1]:
            return [1, 2, 3, 4]
        else:
            return [1, 1, 3, 4]

    if def_bool[2]:
        if def_bool[1]:
            return
        if def_bool[3]:
            return [5, 3, 2, 0]
        else:
            return [5, 5, 2, 1]


# receives a number and returns if its a prime number
def is_prime(num):
    divisor = 2
    while divisor <= num ** .5:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


# receives a number and returns the first 'n' prime numbers in a list
def primes_for_asafi(n):
    lst_primes = []
    if n <= 0:
        return lst_primes
    primes_counter = 0
    num_check = 2
    while primes_counter != n:  # works until the list has 'n' number of primes
        if is_prime(num_check):
            lst_primes.append(num_check)
            primes_counter += 1
        num_check += 1
    return lst_primes


# receives a list of vectors and returns a vector of their summary
def sum_of_vectors(vec_lst):
    vec_sum = []
    summary_vec = 0
    if len(vec_lst) == 0:
        return
    # nested loop which runs through the objects inside vec_lst and summarize them
    for i in range(0, len(vec_lst[0])):
        for j in range(0, len(vec_lst)):
            summary_vec += float(vec_lst[j][i])
        vec_sum.append(summary_vec)
        summary_vec = 0
    return vec_sum


# receives a list of vectors and returns the amount of orthogonal vectors inside
def num_of_orthogonal(vectors):
    orthogonal_amount = 0
    if len(vectors) <= 1:
        return orthogonal_amount
    # nested loop which runs through all pairing options of objects inside 'vectors'
    # to check if their inner product is 0(orthogonal)
    for i in range(0, len(vectors) - 1):
        for j in range(i + 1, len(vectors)):
            if inner_product(vectors[i], vectors[j]) == 0:
                orthogonal_amount += 1
    return orthogonal_amount
