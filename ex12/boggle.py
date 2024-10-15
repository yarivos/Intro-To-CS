import tkinter as tki
from tkinter.constants import GROOVE, RIDGE
from typing import Callable, List
from ex12_utils import *
from boggle_board_randomizer import randomize_board

BUTTON_HOVER_COLOR = 'pink'
REGULAR_COLOR = 'grey'
BUTTON_ACTIVE_COLOR = 'powder blue'
BUTTON_STYLE = {'font': ('Courier', 30), 'borderwidth': 2,
                'bg': REGULAR_COLOR, 'activebackground': BUTTON_ACTIVE_COLOR}


class BoggleGUI:
    def __init__(self, board) -> None:
        self.root = tki.Tk()
        self.root.resizable(False, False)
        self.board = board
        self.button_list = {}
        self.root.title("Boggle")
        self.outer_frame = tki.Frame(self.root)
        self.outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self.frame1 = tki.Frame(self.outer_frame)
        self.frame1.pack()
        self._main_window = self.root
        self.build_grid()
        self._pack_items()

    def build_grid(self):
        for row in range(len(self.board)):  # row iterator
            for column in range(len(self.board[0])):  # column iterator
                current_button = tki.Button(self.frame1, relief=GROOVE,  text=last_letter(self.board, (row, column)), **BUTTON_STYLE)
                self.button_list[(row, column)] = current_button
                current_button.grid(row=row, column=column)
                current_button.configure(command = self.test_func)
                
    @staticmethod
    def test_func(*args, **kwargs):
        print(*args)
        print(**kwargs)
                    
    def set_button_command(self, button_name:str, cmd: Callable[[], None]) -> None:
        self.button_list[button_name].configure(command = cmd)

    def set_label_display(self):
        pass
    
    def get_button_chars(self) -> List[str]:
        pass

    def _pack_items(self):
        pass

    def run_GUI(self):
        self._main_window.mainloop()

class BoggleModel:
    def __init__(self):
        pass


if __name__ == '__main__':
    my_b = randomize_board()
    boogle_gui = BoggleGUI(my_b)
    boogle_gui.run_GUI()

    # test_time1 = time()
    # print(test_time1)
    # test1 = load_words_dict('boggle_dict.txt')
    # my_b = randomize_board()
    # y = find_length_n_words(16, my_b, test1)
    # for x in y:
    #     print(x)
    # how_long = time() - test_time1
    # print(how_long)

