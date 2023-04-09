"""
File with Courtney's code
"""

from tkinter import *
from tkinter import messagebox
from random import *


def main():
    program = RockPaperScissors()
    program.root.mainloop()


class RockPaperScissors:
    # initialize ‘number of objects per team’ value
    # set up background color variable

    def __init__(self):
        self.root = Tk()
        # name window
        # create canvas and interface frames
        # set up ‘scissors’ image as label
        # set up ‘rock’ image as label
        # set up ‘paper’ image as label
        # set up “Set up”, “Start”, and “Stop” buttons
        # initialize “is_running” Boolean as False
        # set up callback functions

    # function to create frames

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


if __name__ == "main":
    main()
