##############################
# FILE:calculate_mathematical_expression.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex2 2021
# DESRIPTION: returning largest and smallest number out of 3 parameters
# the standard output(screen).
##############################
#check values with roots and minus roots.
#check values of type float and quadratic.

def largest_and_smallest(num1, num2, num3):
#returns maximum and minimum value of three parameters
    if num1 >= num2:

        if num1 >= num3:
            max_num = num1

            if num2 >= num3:
                min_num = num3
            else:
                min_num = num2
        else:
            max_num = num3
            min_num = num2

    elif num1 < num2:

        if num2 <= num3:
            max_num = num3
            min_num = num1
        else:
            max_num = num2

            if num1 >= num3:
                min_num = num3
            else:
                min_num = num1

    return max_num, min_num

def check_largest_and_smallest():
#verifies largest_and_smallest function validity with 5 checks
    check1 = (largest_and_smallest(17, 1, 6))
    check2 = (largest_and_smallest(1, 17, 6))
    check3 = (largest_and_smallest(1, 1, 2))
    check4 = (largest_and_smallest(-2, -2.1, (-3)**2))
    check5 = (largest_and_smallest(2**.5, -1**.5, -2**.5))
    if check1 == (17, 1):
        if check2 == (17, 1):
            if check3 == (2, 1):
                if check4 == (9, -2.1):
                    if(check5 == (2**.5, -2**.5)):
                        return True
    return False
