"""
File with finalized code
"""

from tkinter import *
from tkinter import messagebox
from random import *


def main():
    program = RockPaperScissors()
    program.root.mainloop()


class RockPaperScissors:
    def __init__(self):
        self.root = Tk()


if __name__ == "main":
    main()
