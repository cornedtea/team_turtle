"""
File with Courtney's code
"""

from mainCode import *
from tkinter import *
from tkinter import messagebox
from random import *


def main():
    program = RockPaperScissors()
    program.root.mainloop()


class RockPaperScissors:
    team_size = 2
    canvas_bg_color = "#a3afbf"  # bluish grey color
    interface_bg_color = "#b1b6bd"  # greyish color

    def __init__(self):
        self.root = Tk()
        self.root.title = "Rock Paper Scissors"
        screensize = str(self.root.winfo_screenwidth() - 50) + "x" + str(self.root.winfo_screenheight() - 50)
        self.root.geometry(screensize + "+0+5")
        self.canvas_frame, self.interface_frame = self.create_frames()
        # set up ‘scissors’ image as label
        # set up ‘rock’ image as label
        # set up ‘paper’ image as label
        # set up “Set up”, “Start”, and “Stop” buttons
        self.is_running = False
        # set up callback functions

    def create_frames(self):
        """ Creates canvas and interface frames."""
        interface_frame = Frame(self.root, bg=RockPaperScissors.interface_bg_color)
        interface_frame.pack(fill="both", expand=True)

        canvas_frame = Canvas(self.root, bg=RockPaperScissors.canvas_bg_color)
        canvas_frame.pack(fill="both", expand=True)
        return canvas_frame, interface_frame

    # button functions

    # callback functions

    # animation function

    # collision function

    def endResult(self):
        # save name of winning team as ‘winner’
        #if guess is the same as ‘winner’:
        #     messagebox with congratulatory message
        # else:
        #     message box with better luck next time message
        pass


if __name__ == "__main__":
    main()
