import tkinter as tki
from datetime import datetime

H24_MODE = 24
H12_MODE = 12


class ClockGUI:

    def __init__(self, clock_model):
        self._clock_model = clock_model
        self._root = tki.Tk()
        self._clock_display = tki.Label(font=("Courier", 30), width=11)
        self._clock_display.pack()

        # just to demo binding on the label:
        self._clock_display.bind("<Button-1>", self._label_clicked)

        self._button = tki.Button(text="mode", font=("Courier", 30))
        self._button.pack()
        self._button["command"] = self._clock_model.switch_mode

    def _label_clicked(self, event):
        print(event.x, event.y)
        print(dir(event))

    def _animate(self):
        self._clock_display["text"] = self._clock_model.get_time_str()
        self._root.after(10, self._animate)

    def run(self):
        self._animate()
        self._root.mainloop()


class ClockModel:
    def __init__(self, mode=H24_MODE):
        self._mode = mode

    def switch_mode(self):
        if self._mode is H12_MODE:
            self._mode = H24_MODE
        else:
            self._mode = H12_MODE

    def get_time_str(self):
        now = datetime.now()
        if self._mode is H24_MODE:
            return now.strftime("%H:%M:%S:%f")[:-4]
        else:
            return now.strftime("%p %I:%M:%S")



class FakeModel:
"""an empty implementation of the API of the clock model used for testing."""
    def switch_mode(self):
        pass

    def get_time_str(self):
        return "Fake"


if __name__ == "__main__":
    # we can run the clock model on its own:
    # print(ClockModel().get_time_str())

    # we can run the GUI on its own by providing a fake model
    # ClockGUI(FakeModel()).run()

    # or we can run the application as intended:
    ClockGUI(ClockModel()).run()