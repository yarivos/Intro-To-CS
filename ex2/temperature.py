##############################
# FILE:temperature.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex2 2021
# DESRIPTION: function for finding if at least 2 parameters are bigger then min_temp
# the standard output(screen).
##############################

def is_it_summer_yet(min_temp, temp_day1, temp_day2, temp_day3):
#returns if two of the parameters are bigger than min_temp
    if min_temp >= temp_day1 and min_temp >= temp_day2:
        return False
    elif min_temp >= temp_day1 and min_temp >= temp_day3:
        return False
    elif min_temp >= temp_day2 and min_temp >= temp_day3:
        return False
    return True


