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


class Rock:
    def __init__(self):
        self.name = "Rock"
        self.image = PhotoImage(file="Images/rock.jpg")

    def getType(self):
        return self.name

    def getImage(self):
        return self.image


class Paper:
    def __init__(self):
        self.name = "Paper"
        self.image = PhotoImage(file="Images/paper.jpg")

    def getType(self):
        return self.name

    def getImage(self):
        return self.image


class Scissors:
    def __init__(self):
        self.name = "Scissors"
        self.image = PhotoImage(file="Images/scissors.png")

    def getType(self):
        return self.name

    def getImage(self):
        return self.image


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
        self.teamRock = create_team("Rock")
        self.teamPaper = create_team("Paper")
        self.teamScissors = create_team("Scissors")
        self.setup_button, self.start_button, self.quit_button = self.create_buttons()
        self.is_running = False
        self.set_callbacks()
        self.winner = None
        self.userguess = None

    def create_frames(self):
        """ Creates canvas and interface frames."""
        interface_frame = Frame(self.root, height=50, bg=RockPaperScissors.interface_bg_color)
        interface_frame.pack(fill="x")

        canvas_frame = Canvas(self.root, bg=RockPaperScissors.canvas_bg_color, bd=0)
        canvas_frame.pack(fill="both", expand=True)
        return canvas_frame, interface_frame

    def create_buttons(self):
        spacer = Label(self.interface_frame, text="", bg=RockPaperScissors.interface_bg_color)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        setup_button = Button(self.interface_frame, text="Set up")
        setup_button.pack(side=LEFT, padx=20, pady=10)
        start_button = Button(self.interface_frame, text="Start")
        start_button.pack(side=LEFT, padx=20, pady=10)
        quit_button = Button(self.interface_frame, text="Quit")
        quit_button.pack(side=LEFT, padx=20, pady=10)
        spacer = Label(self.interface_frame, text="", bg=RockPaperScissors.interface_bg_color)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        return setup_button, start_button, quit_button

    def set_callbacks(self):
        self.setup_button['command'] = self.setup
        self.start_button['command'] = self.start
        self.quit_button['command'] = self.quit

    def guess(self):  # TODO
        """ Provides window for user to guess which team will win."""
        guess = self.teamRock
        return guess

    def setup(self):  # TODO
        """ Sets up simulation."""
        self.winner = None
        self.userguess = self.guess()

    def start(self):  # TODO
        if self.start_button['text'] == "Start":
            self.is_running = True
            self.start_button['text'] = "Stop"
        else:
            self.is_running = False
            self.start_button['text'] = "Start"

    def quit(self):
        really_quit = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if really_quit:
            self.root.destroy()

    # animation function

    def collision(self, obj1, obj2):  # TODO
        """ Determines team transfer on collision."""
        if obj1.getType() == "Paper" and obj2.getType == "Rock":
            pass
        if RockPaperScissors.team_size == RockPaperScissors.team_size * 3:
            self.is_running = False
        pass

    def determineWinner(self):  # TODO
        teams = [self.teamRock, self.teamPaper, self.teamScissors]
        winner = choice(teams)
        return winner

    def endResult(self):
        """ Creates message telling user if their guess was correct."""
        self.winner = self.determineWinner()
        if self.userguess == self.winner:
            messagebox.showinfo("Result", "Congratulations! You guessed {} and {} won."
                                .format(self.userguess, self.winner))
        else:
            messagebox.showinfo("Result", "You guessed {}, but {} won. Better luck next time!"
                                .format(self.userguess, self.winner))


def create_team(teamname):  # TODO
    team = []
    for i in range(RockPaperScissors.team_size):
        if teamname == "Rock":
            new = Rock()
        elif teamname == "Paper":
            new = Paper()
        else:
            new = Scissors()
        team.append(new)
    return team


if __name__ == "__main__":
    main()
