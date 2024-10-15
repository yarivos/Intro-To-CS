##############################
# FILE:hello_turtle.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex1 2021
# DESRIPTION: use of turtle function to draw a flowers.
# the standard output(screen).
##############################

#this line imports turtle package
import turtle

def draw_petal(): #this line creates a new function named: draw_petal
    #this next line draw a petal
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower(): #this line creates a new function named: draw_flower

    #this next lines use function draw_petal in order to draw a flower
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

#the next line creates a new function named draw_flower_and_advance
def draw_flower_and_advance():

    #this next lines use draw_flower and advances "turtle" to the next flower starting spot
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

#this next line creates a function called draw_flower_bed
def draw_flower_bed():

    #this next lines flip the drawing of the function upside down
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    #this next lines call the function draw_flower_and_advance three times
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__=="__main__":
    draw_flower_bed()
    turtle.done()