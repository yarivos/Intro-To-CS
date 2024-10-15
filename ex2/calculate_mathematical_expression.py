##############################
# FILE:calculate_mathematical_expression.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex2 2021
# DESRIPTION: calculates a mathematical expression
# the standard output(screen).
##############################

def calculate_mathematical_expression(num1, num2, operation):
# next lines check which operation to use with num1 and num2 and return the correct value
      if operation == '+':
        return num1 + num2
      elif operation == '-':
        return num1 - num2
      elif operation == '*':
        return num1 * num2
      elif operation == ':':
        if num2 != 0:
            return num1 / num2



# def calculate_from_string(expression):
# #splits the string input into their correct parameters
#     num1, operation, num2 = expression.split()
#     num1 = float(num1)
#     num2 = float(num2)
#     #uses calculate_mathematical_expression function to return the input value._
#     return calculate_mathematical_expression(num1, num2, operation)

