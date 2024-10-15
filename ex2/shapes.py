##############################
# FILE:calculate_mathematical_expression.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex2 2021
# DESRIPTION: returns area of shapes
# the standard output(screen).
##############################
import math
def shape_area():
    user_shape = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if user_shape != 1 and user_shape != 2 and user_shape != 3:
        return          #if user input wrong value
    #next lines check the shape and return the area of shape
    if user_shape == 1:
        radius = float(input())
        return (radius ** 2) * math.pi
    elif user_shape == 2:
        edge1 = float(input())
        edge2 = float(input())
        return edge1 * edge2
    else:
        tri_edge = float(input())
        return ((math.sqrt(3)/4)*(tri_edge**2))

