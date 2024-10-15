import tkinter as tki
from typing import Iterable

def callback(): 
    print('CLICKED!')
    label1.configure(text = 'clicked. ')

root = tki.Tk()
button1 = tki.Button(root, command=callback, text = "WTF?", font = ("Courier", 30))
button1.pack()
label1 = tki.Label(root, text = 'lets finish this...', font = ("Courier", 30))
label1.pack()
frame1 = tki.Frame(root)
frame1.pack(side = tki.LEFT)


for i in range(5):
    b = tki.Button(frame1, text = 'botton' + str(i), font = ("Courier", 30))
    b.pack()


root.mainloop()

#INTERACTIVE CLASS
def my_filter(func, iter):
    return (item for item in iter if func(item)) #GENERATOR COMPREHENSION
    # for item in iter: 
    #     if func(item):
    #         yield item 

y = my_filter(lambda x: x % 2 == 0, range(10))
# print(*y)

class MyFilter: 
    # this is without a generator, 
    # exactly what we did in 1 line earlier (line 20)
    def __init__(self, func, it):
        self.__func = func 
        self.__iterable = iter(it)

#aviv: RANGE 10 IS ITERABLE BUT IS NOT AN ITERATOR #
    def __iter__(self):
        return self 

    def __next__(self):
        item = next(self.__iterable)
        while not self.__func(item):
            item = next(self.__iterable)
        return item 

Z = MyFilter(lambda x: x % 2 == 0, range(10))
#WE NEED TO REMEMBER THE SENTINEL 
# print(*Z)