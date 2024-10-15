import tkinter as tki
import sys
from tkinter.constants import GROOVE, RIDGE
from typing import Callable, List, Dict, Any
from ex12_utils import *
from boggle_board_randomizer import randomize_board
from tkinter import messagebox

EXIT_TITLE = "EXIT"
BUTTON_HOVER_COLOR = 'pink'
REGULAR_COLOR = 'grey'
BUTTON_ACTIVE_COLOR = 'powder blue'
BUTTON_STYLE = {'font': ('Courier', 30), 'borderwidth': 2,
                'bg': REGULAR_COLOR, 'activebackground': BUTTON_ACTIVE_COLOR}
EXIT_MSG = "THANK YOU FOR PLAYING! SEE YOU AGAIN SOON!"


class BoggleGUI:
    _buttons: Dict[str, tki.Button] = {}

    def __init__(self) -> None:
        root = tki.Tk()
        root.title("Boggle")
        root.resizable(False, False)
        self._main_window = root
        self._outer_frame = tki.Frame(root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._buttons_frame = tki.Frame(self._outer_frame)  # Right frame
        self._buttons_frame.pack(side=tki.RIGHT, fill=tki.BOTH, expand=True)
        self._exit_button = tki.Button(self._buttons_frame, text='EXIT', **BUTTON_STYLE, command=self._exit)
        self._score_label = tki.Label(self._buttons_frame, **BUTTON_STYLE)  ## THE LABEL WITH THE SCORE
        self._timer_label = tki.Label(self._buttons_frame, **BUTTON_STYLE)  ## THE LABEL WITH THE TIMER

        self._letters_frame = tki.Frame(self._outer_frame)
        self._letters_frame.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)
        self._create_letter_buttons()  # TODO
        self._pack_widgets()

    def _pack_widgets(self):
        self._exit_button.pack()
        self._score_label.pack()
        self._timer_label.pack()

    def _exit(self):
        messagebox.showinfo(title=EXIT_TITLE, message=EXIT_MSG)
        sys.exit()

    def _create_letter_buttons(self):
        for i in range(4):
            tki.Grid.columnconfigure(self._letters_frame, i, weight=1)  # type: ignore
        for i in range(5):
            tki.Grid.rowconfigure(self._letters_frame, i, weight=1)  # type: ignore
        self._make_letter_button("C", 0, 0)
        self._make_letter_button("/", 0, 1)
        self._make_letter_button("*", 0, 2)
        self._make_letter_button("-", 0, 3)
        self._make_letter_button("7", 1, 0)
        self._make_letter_button("8", 1, 1)
        self._make_letter_button("9", 1, 2)
        self._make_letter_button("+", 1, 3)
        self._make_letter_button("4", 2, 0)
        self._make_letter_button("5", 2, 1)
        self._make_letter_button("6", 2, 2)
        self._make_letter_button("C", 2, 3)
        self._make_letter_button("1", 3, 0)
        self._make_letter_button("2", 3, 1)
        self._make_letter_button("3", 3, 2)
        self._make_letter_button("=", 3, 3)


    def _make_letter_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tki.Button:
        button = tki.Button(self._letters_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._buttons[button_char] = button

        def _on_enter(event: Any) -> None:
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event: Any) -> None:
            button['background'] = REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        return button

    def build_grid(self):
        pass

    def run_GUI(self):
        self._main_window.mainloop()


class BoggleModel:
    def __init__(self, board):
        pass


if __name__ == '__main__':
    # my_b = randomize_board()
    boogle_gui = BoggleGUI()
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

