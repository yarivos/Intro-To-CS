##############################
# FILE:calculate_mathematical_expression.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex2 2021
# DESRIPTION: returns solutions to quadratic equation
# the standard output(screen).
##############################

import math
def quadratic_equation(a, b, c):
#function which returns the solutions of quadratic equation
    if ((b**2)-4*a*c) == 0:      #if the expression is true the equation has one solution
         return (-b)/(2*a), None

    elif ((b**2)-4*a*c) > 0:     #if the expression is true the equation has 2 solutions
         sol1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
         sol2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
         return sol1, sol2

    else:                        #if there are no solutions to the quadratic equation
         return


def quadratic_equation_user_input():
#receive 3 parameters from user and returns quadratic equation solution of three parameters
    user_input = input('Insert coefficients a, b, and c: ')
    a, b, c = user_input.split()
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        return print("The parameter "+"'a'"+" may not equal 0")
    eq_sol = quadratic_equation(a, b, c)

    if eq_sol == None:           #if there are no solutions for quadratic equation
        return print('The equation has no solutions')

    else:
        sol1 = eq_sol[0]
        sol2 = eq_sol[1]
        if sol2 == None:               #prints the solutions
            return print('The equation has 1 solution: ' + str(sol1))
        else:
            return print('The equation has 2 solutions: ' + str(sol1) + ' and ' + str(sol2))



