##############################
# FILE:math_print.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex1 2021
# DESRIPTION: use of math fuctions
# the standard output(screen).
##############################

import math
#imports math package

#creates a function which prints the golden ratio
def golden_ratio():
    print((1+math.sqrt(5))/2) #prints the calculation of the golden ratio

def six_squared(): #creates a function which prints the number 6 raised to the power 2
    print(math.pow(6,2)) #print the calculation of six raised to the power 2

def hypotenuse():
#creates a function which prints the length of the hypotenuse
    print(math.sqrt(math.pow(5,2)+math.pow(12,2)))

def pi(): #creates a function which prints the value of pi
    print(math.pi)

def e(): #creates a function name e() which prints the value of e
    print(math.e)

def squares_area(): #creates a function which prints squares area
    print(1*1,2*2,3*3,4*4,5*5,6*6,7*7,8*8,9*9,10*10)

if __name__=="__main__":
    golden_ratio() #uses the function golden_ratio()
    six_squared()#uses the function six_squared()
    hypotenuse()#uses the function hypotenuse
    pi()    # uses the function pi()
    e()     #uses the function e()
    squares_area() #uses the function squares_area()




