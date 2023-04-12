"""
File with Courtney's code
"""

from mainCode import *
from tkinter import *
from tkinter import messagebox
from random import *
from time import *


def main():
    program = RockPaperScissors()
    program.root.mainloop()


class RockPaperScissors:
    team_size = 1
    canvas_bg_color = "#a3afbf"  # bluish grey color
    interface_bg_color = "#b1b6bd"  # greyish color

    class Movable:
        def __init__(self, team: str):
            self.name = team
            self.x_movement = 5
            self.y_movement = 5
            self.width = 0
            self.height = 0
            self.image = self.setImage()

        def getType(self):
            """ Returns the type of the Movable object as a string."""
            return self.name

        def setType(self, team: str):
            self.name = team

        def setImage(self):
            """ Sets the image of the object based on the team name."""
            if self.name == "Rock":
                image = PhotoImage(file="Images/rock.png")
                image = image.zoom(2)
                image = image.subsample(9)
            elif self.name == "Paper":
                image = PhotoImage(file="Images/paper.png")
            else:
                image = PhotoImage(file="Images/scissors.png")
                image = image.zoom(2)
                image = image.subsample(9)
            self.width = image.width()
            self.height = image.height()
            return image

        def place(self, canvas, width, height):
            startx = randrange(width)
            starty = randrange(height)
            canvas_object = canvas.create_image(startx, starty, image=self.image)
            return canvas_object

    def __init__(self):
        self.root = Tk()
        self.root.title = "Rock Paper Scissors"
        self.window_width = self.root.winfo_screenwidth() - 50
        self.window_height = self.root.winfo_screenheight() - 100
        screensize = str(self.window_width) + "x" + str(self.window_height)
        self.root.geometry(screensize + "+0+5")
        self.root.resizable(FALSE, FALSE)
        self.canvas_frame, self.interface_frame = self.create_frames()
        self.teamRock = []
        self.teamPaper = []
        self.teamScissors = []
        self.rockObjs = []
        self.paperObjs = []
        self.scissorsObjs = []
        self.objs = {}
        self.setup_button, self.start_button, self.guess_label, self.quit_button = self.create_widgets()
        self.is_running = False
        self.userguess = StringVar()
        self.winner = None
        self.set_callbacks()

    def create_frames(self):
        """ Creates canvas and interface frames."""
        interface_frame = Frame(self.root, height=50, bg=RockPaperScissors.interface_bg_color)
        interface_frame.pack(fill="x")

        canvas_frame = Canvas(self.root, bg=RockPaperScissors.canvas_bg_color, bd=0)
        canvas_frame.pack(fill="both", expand=True)
        return canvas_frame, interface_frame

    def create_widgets(self):
        spacer = Label(self.interface_frame, text="", bg=RockPaperScissors.interface_bg_color)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        setup_button = Button(self.interface_frame, text="Set up")
        setup_button.pack(side=LEFT, padx=20, pady=10)
        start_button = Button(self.interface_frame, text="Start")
        start_button.pack(side=LEFT, padx=20, pady=10)
        guess_label = Label(self.interface_frame, text="Your guess: ")
        guess_label.pack(side=LEFT, padx=20, pady=10)
        quit_button = Button(self.interface_frame, text="Quit")
        quit_button.pack(side=LEFT, padx=20, pady=10)
        spacer = Label(self.interface_frame, text="", bg=RockPaperScissors.interface_bg_color)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        return setup_button, start_button, guess_label, quit_button

    def create_teams(self):
        """ Creates teams of equal size, one each of rock, paper, and scissors."""
        teamRock = []
        teamPaper = []
        teamScissors = []
        for i in range(RockPaperScissors.team_size):
            newRock = self.Movable("Rock")
            teamRock.append(newRock)
            newPaper = self.Movable("Paper")
            teamPaper.append(newPaper)
            newScissors = self.Movable("Scissors")
            teamScissors.append(newScissors)
        return teamRock, teamPaper, teamScissors

    def set_callbacks(self):
        self.setup_button['command'] = self.setup
        self.start_button['command'] = self.start
        self.quit_button['command'] = self.quit

    def guess(self):
        """ Provides window for user to guess which team will win."""
        popup = Tk()
        self.userguess = StringVar(popup)
        radiorock = Radiobutton(popup, text="Rock", variable=self.userguess,
                                value="Rock", command=self.display_guess)
        radiorock.grid(row=0, column=0, sticky=W)
        radiopaper = Radiobutton(popup, text="Paper", variable=self.userguess,
                                 value="Paper", command=self.display_guess)
        radiopaper.grid(row=0, column=1, sticky=W)
        radioscissors = Radiobutton(popup, text="Scissors", variable=self.userguess,
                                    value="Scissors", command=self.display_guess)
        radioscissors.grid(row=0, column=2, sticky=W)
        spacer = Label(popup)
        spacer.grid(row=1, column=0)
        submit_button = Button(popup, text="Submit")
        submit_button.grid(row=1, column=1)
        submit_button['command'] = popup.destroy
        spacer = Label(popup)
        spacer.grid(row=1, column=2)

    def display_guess(self):
        """ Using this to test guess()"""
        self.guess_label['text'] = "Your guess: {}".format(self.userguess.get())
        
    def populate(self):
        """ Places objects from teams onto canvas. The object lists keeps track of
        the canvas representations of the objects."""
        rockObjs = []
        paperObjs = []
        scissorsObjs = []
        for obj in self.teamRock:
            rock = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            rockObjs.append(rock)
        for obj in self.teamPaper:
            paper = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            paperObjs.append(paper)
        for obj in self.teamScissors:
            scissors = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            scissorsObjs.append(scissors)
        return rockObjs, paperObjs, scissorsObjs

    def setup(self):
        """ Sets up simulation."""
        self.winner = None
        self.guess_label['text'] = "Your guess: "
        self.canvas_frame.delete('all')
        self.teamRock, self.teamPaper, self.teamScissors = self.create_teams()
        self.rockObjs, self.paperObjs, self.scissorsObjs = self.populate()
        for i in range(RockPaperScissors.team_size):
            self.objs[self.teamRock[i]] = self.rockObjs[i]
            self.objs[self.teamPaper[i]] = self.paperObjs[i]
            self.objs[self.teamScissors[i]] = self.scissorsObjs[i]
        self.guess()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_button['text'] = "Stop"
            self.canvas_frame.after(100, self.animate())
        else:
            self.is_running = False
            self.start_button['text'] = "Start"

    def quit(self):
        really_quit = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if really_quit:
            self.root.destroy()

    def animate(self):
        while self.is_running:
            for team in [zip(self.teamRock, self.rockObjs), zip(self.teamPaper, self.paperObjs),
                         zip(self.teamScissors, self.scissorsObjs)]:
                for obj, canvobj in team:
                    self.canvas_frame.move(canvobj, obj.x_movement, obj.y_movement)
                    self.root.update()
                    obj_pos = self.canvas_frame.coords(canvobj)
                    xc, yc = obj_pos
                    if xc < abs(obj.width) / 2 or xc > self.window_width - abs(obj.height) / 2:
                        obj.x_movement = -obj.x_movement
                    if yc < abs(obj.width) / 2 or yc > (self.window_height - 50) - abs(obj.height) / 2:
                        obj.y_movement = -obj.y_movement
                    collided, collidees = self.detectCollision(canvobj)
                    if collided:
                        obj.x_movement = -obj.x_movement
                        obj.y_movement = -obj.y_movement
                        for collidee in collidees:
                            self.collision(obj, collidee)
            sleep(0.01)

    def detectCollision(self, canvobj):
        zone = self.canvas_frame.bbox(canvobj)
        nearcanvobjs = self.canvas_frame.find_overlapping(zone[0], zone[1], zone[2], zone[3])
        nearcanvobjs = list(nearcanvobjs)
        nearcanvobjs.remove(canvobj)
        if len(nearcanvobjs) != 0:
            collided = True
        else:
            collided = False
        return collided, nearcanvobjs

    def collision(self, obj1, canvobj2):
        """ Determines team transfer on collision."""
        val_list = list(self.objs.values())
        key_list = list(self.objs.keys())
        position = val_list.index(canvobj2)
        obj2 = key_list[position]
        if obj1.getType() == "Rock" and obj2.getType() == "Paper":
            winner = obj2
            self.teamRock.remove(obj1)
            self.rockObjs.remove(self.objs[obj1])
            self.teamPaper.append(obj1)
            self.paperObjs.append(self.objs[obj1])
            obj1.setType("Paper")
        elif obj1.getType() == "Rock" and obj2.getType() == "Scissors":
            winner = obj1
            self.teamScissors.remove(obj2)
            self.scissorsObjs.remove(self.objs[obj2])
            self.teamRock.append(obj2)
            self.rockObjs.append(self.objs[obj2])
            obj2.setType("Rock")
        elif obj1.getType() == "Paper" and obj2.getType() == "Rock":
            winner = obj1
            self.teamRock.remove(obj2)
            self.rockObjs.remove(self.objs[obj2])
            self.teamPaper.append(obj2)
            self.paperObjs.append(self.objs[obj2])
            obj2.setType("Paper")
        elif obj1.getType() == "Paper" and obj2.getType() == "Scissors":
            winner = obj2
            self.teamPaper.remove(obj1)
            self.paperObjs.remove(self.objs[obj1])
            self.teamScissors.append(obj1)
            self.scissorsObjs.append(self.objs[obj1])
            obj1.setType("Scissors")
        elif obj1.getType() == "Scissors" and obj2.getType() == "Rock":
            winner = obj2
            self.teamScissors.remove(obj1)
            self.scissorsObjs.remove(self.objs[obj1])
            self.teamRock.append(obj1)
            self.rockObjs.append(self.objs[obj1])
            obj1.setType("Rock")
        elif obj1.getType() == "Scissors" and obj2.getType() == "Paper":
            winner = obj1
            self.teamPaper.remove(obj2)
            self.paperObjs.remove(self.objs[obj2])
            self.teamScissors.append(obj2)
            self.scissorsObjs.append(self.objs[obj2])
            obj2.setType("Scissors")
        else:
            winner = None
        self.canvas_frame.itemconfig(self.objs[obj1], image=obj1.image)
        self.canvas_frame.itemconfig(self.objs[obj2], image=obj2.image)
        if winner in self.teamRock:
            winner_team = self.teamRock
        elif winner in self.teamPaper:
            winner_team = self.teamPaper
        elif winner in self.teamScissors:
            winner_team = self.teamScissors
        else:
            winner_team = []
        if len(winner_team) == RockPaperScissors.team_size * 3:
            self.is_running = False
            if winner_team == self.teamRock:
                self.winner = "Rock"
            elif winner_team == self.teamPaper:
                self.winner = "Paper"
            elif winner_team == self.teamScissors:
                self.winner = "Scissors"
            self.endResult()

    def endResult(self):
        """ Creates message telling user if their guess was correct."""
        if self.userguess.get() == self.winner:
            messagebox.showinfo("Result", "Congratulations! You guessed {} and {} won."
                                .format(self.userguess.get(), self.winner))
        else:
            messagebox.showinfo("Result", "You guessed {}, but {} won. Better luck next time!"
                                .format(self.userguess.get(), self.winner))


if __name__ == "__main__":
    main()
