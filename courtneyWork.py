"""
Courtney's Code -- v1.0.2

v1.0.2 Updates:
-- NEW: changes to variable names to follow underscore format
-- 'Set up' button changes to 'Reset' when pressed
-- combine Rock, Paper, and Scissors into one class Movable, which is nested in RockPaperScissors

Possible Changes:
-- more intuitive UI
-- slider for team size
-- images scale size based on team size
-- radio buttons unselected on start
-- make `overlap` not static
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
    team_size = 3
    canvas_bg_color = '#a3afbf'  # bluish grey color
    interface_bg_color = '#b1b6bd'  # grey-ish color

    class Movable:
        def __init__(self, team: str = 'Rock' or 'Paper' or 'Scissors'):
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
            self.image = self.setImage()

        def setImage(self):
            """ Sets the image of the object based on the team name."""
            if self.name == 'Rock':
                image = PhotoImage(file='Images/rock.png')
                image = image.zoom(2)
                image = image.subsample(9)
            elif self.name == 'Paper':
                image = PhotoImage(file='Images/paper.png')
            else:
                image = PhotoImage(file='Images/scissors.png')
                image = image.zoom(2)
                image = image.subsample(9)
            self.width = image.width()
            self.height = image.height()
            return image

        def place(self, canvas, width, height):
            start_x = randrange(self.width // 2 + 10, width - self.width // 2 - 10)
            start_y = randrange(self.height // 2 + 10, height - self.height // 2 - 10)
            object_ID = canvas.create_image(start_x, start_y, image=self.image)
            collided = self.overlap(canvas, object_ID)
            while collided:
                canvas.delete(object_ID)
                start_x = randrange(self.width // 2, width - self.width // 2)
                start_y = randrange(self.height // 2, height - self.height // 2)
                object_ID = canvas.create_image(start_x, start_y, image=self.image)
                collided = self.overlap(canvas, object_ID)
            return object_ID
        
        def overlap(self, canvas, object_ID):
            zone = canvas.bbox(object_ID)
            near_object_IDs = canvas.find_overlapping(zone[0], zone[1], zone[2], zone[3])
            near_object_IDs = list(near_object_IDs)
            near_object_IDs.remove(object_ID)
            if len(near_object_IDs) != 0:
                overlap = True
            else:
                overlap = False
            return overlap

    def __init__(self):
        self.root = Tk()
        self.root.title = 'Rock Paper Scissors'
        self.window_width = self.root.winfo_screenwidth() - 50
        self.window_height = self.root.winfo_screenheight() - 100
        screensize = str(self.window_width) + 'x' + str(self.window_height)
        self.root.geometry(screensize + '+0+5')
        self.root.resizable(FALSE, FALSE)
        self.canvas_frame, self.interface_frame = self.create_frames()
        self.rock_objects = []
        self.paper_objects = []
        self.scissors_objects = []
        self.rock_IDs = []
        self.paper_IDs = []
        self.scissors_IDs = []
        self.objects = {}
        self.setup_button, self.start_button, self.guess_label, self.quit_button = self.create_widgets()
        self.is_running = False
        self.user_guess = StringVar()
        self.winner = None
        self.set_callbacks()

    def create_frames(self):
        """ Creates canvas and interface frames."""
        interface_frame = Frame(self.root, height=50, bg=RockPaperScissors.interface_bg_color)
        interface_frame.pack(fill='x')

        canvas_frame = Canvas(self.root, bg=RockPaperScissors.canvas_bg_color, bd=0)
        canvas_frame.pack(fill='both', expand=True)
        return canvas_frame, interface_frame

    def create_widgets(self):
        spacer = Label(self.interface_frame, text='', bg=RockPaperScissors.interface_bg_color)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        setup_button = Button(self.interface_frame, text='Set up')
        setup_button.pack(side=LEFT, padx=20, pady=10)
        start_button = Button(self.interface_frame, text='---')
        start_button.pack(side=LEFT, padx=20, pady=10)
        guess_label = Label(self.interface_frame, text='No guess made.')
        guess_label.pack(side=LEFT, padx=20, pady=10)
        quit_button = Button(self.interface_frame, text='Quit')
        quit_button.pack(side=LEFT, padx=20, pady=10)
        spacer = Label(self.interface_frame, text='', bg=RockPaperScissors.interface_bg_color)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        return setup_button, start_button, guess_label, quit_button

    def create_teams(self):
        """ Creates teams of equal size, one each of rock, paper, and scissors."""
        rock_objects = []
        paper_objects = []
        scissors_objects = []
        for i in range(RockPaperScissors.team_size):
            newRock = self.Movable('Rock')
            rock_objects.append(newRock)
            newPaper = self.Movable('Paper')
            paper_objects.append(newPaper)
            newScissors = self.Movable('Scissors')
            scissors_objects.append(newScissors)
        return rock_objects, paper_objects, scissors_objects

    def set_callbacks(self):
        self.setup_button['command'] = self.setup
        self.start_button['command'] = self.start
        self.quit_button['command'] = self.quit

    def guess(self):
        """ Provides window for user to guess which team will win."""
        popup = Tk()
        self.user_guess = StringVar(popup, value=' ')
        question = Label(popup, text='Who do you think will win?')
        question.grid(row=0, column=0, columnspan=3)
        radio_rock = Radiobutton(popup, text='Rock', variable=self.user_guess,
                                 value='Rock', command=self.display_guess)
        radio_rock.grid(row=1, column=0, sticky=W)
        radio_paper = Radiobutton(popup, text='Paper', variable=self.user_guess,
                                  value='Paper', command=self.display_guess)
        radio_paper.grid(row=1, column=1, sticky=W)
        radio_scissors = Radiobutton(popup, text='Scissors', variable=self.user_guess,
                                     value='Scissors', command=self.display_guess)
        radio_scissors.grid(row=1, column=2, sticky=W)
        spacer = Label(popup)
        spacer.grid(row=2, column=0)
        submit_button = Button(popup, text='Submit')
        submit_button.grid(row=2, column=1)
        submit_button['command'] = popup.destroy
        spacer = Label(popup)
        spacer.grid(row=2, column=2)

    def display_guess(self):
        """ Using this to test guess()"""
        self.guess_label['text'] = 'Your guess: {}'.format(self.user_guess.get())
        
    def populate(self):
        """ Places objects from teams onto canvas. The object lists keeps track of
        the canvas representations of the objects."""
        rock_IDs = []
        paper_IDs = []
        scissors_IDs = []
        for obj in self.rock_objects:
            rock = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            rock_IDs.append(rock)
        for obj in self.paper_objects:
            paper = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            paper_IDs.append(paper)
        for obj in self.scissors_objects:
            scissors = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            scissors_IDs.append(scissors)
        return rock_IDs, paper_IDs, scissors_IDs

    def setup(self):
        """ Sets up simulation."""
        self.winner = None
        self.guess_label['text'] = 'Your guess: '
        self.canvas_frame.delete('all')
        self.rock_objects, self.paper_objects, self.scissors_objects = self.create_teams()
        self.rock_IDs, self.paper_IDs, self.scissors_IDs = self.populate()
        for i in range(RockPaperScissors.team_size):
            self.objects[self.rock_objects[i]] = self.rock_IDs[i]
            self.objects[self.paper_objects[i]] = self.paper_IDs[i]
            self.objects[self.scissors_objects[i]] = self.scissors_IDs[i]
        self.guess()
        self.start_button['text'] = 'Start'
        self.setup_button['text'] = 'Reset'

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_button['text'] = 'Stop'
            self.canvas_frame.after(100, self.animate())
        else:
            self.is_running = False
            self.start_button['text'] = 'Start'

    def quit(self):
        really_quit = messagebox.askyesno('Quit', 'Are you sure you want to quit?')
        if really_quit:
            self.root.destroy()

    def animate(self):
        while self.is_running:
            for team in [zip(self.rock_objects, self.rock_IDs), zip(self.paper_objects, self.paper_IDs),
                         zip(self.scissors_objects, self.scissors_IDs)]:
                for obj, object_ID in team:
                    self.canvas_frame.move(object_ID, obj.x_movement, obj.y_movement)
                    self.root.update()
                    obj_pos = self.canvas_frame.coords(object_ID)
                    xc, yc = obj_pos
                    if xc < abs(obj.width) / 2 or xc > self.window_width - abs(obj.height) / 2:
                        obj.x_movement = -obj.x_movement
                    if yc < abs(obj.width) / 2 or yc > (self.window_height - 50) - abs(obj.height) / 2:
                        obj.y_movement = -obj.y_movement
                    collided, colliders = self.detectCollision(object_ID)
                    if collided:
                        obj.x_movement = -obj.x_movement
                        obj.y_movement = -obj.y_movement
                        for collider in colliders:
                            self.collision(obj, collider)
            sleep(0.01)

    def detectCollision(self, object_ID):
        zone = self.canvas_frame.bbox(object_ID)
        near_object_IDs = self.canvas_frame.find_overlapping(zone[0], zone[1], zone[2], zone[3])
        near_object_IDs = list(near_object_IDs)
        near_object_IDs.remove(object_ID)
        if len(near_object_IDs) != 0:
            collided = True
        else:
            collided = False
        return collided, near_object_IDs

    def collision(self, obj1, object_ID2):
        """ Determines team transfer on collision."""
        val_list = list(self.objects.values())
        key_list = list(self.objects.keys())
        position = val_list.index(object_ID2)
        obj2 = key_list[position]
        if obj1.getType() == 'Rock' and obj2.getType() == 'Paper':
            winner = obj2
            self.rock_objects.remove(obj1)
            self.rock_IDs.remove(self.objects[obj1])
            self.paper_objects.append(obj1)
            self.paper_IDs.append(self.objects[obj1])
            obj1.setType('Paper')
        elif obj1.getType() == 'Rock' and obj2.getType() == 'Scissors':
            winner = obj1
            self.scissors_objects.remove(obj2)
            self.scissors_IDs.remove(self.objects[obj2])
            self.rock_objects.append(obj2)
            self.rock_IDs.append(self.objects[obj2])
            obj2.setType('Rock')
        elif obj1.getType() == 'Paper' and obj2.getType() == 'Rock':
            winner = obj1
            self.rock_objects.remove(obj2)
            self.rock_IDs.remove(self.objects[obj2])
            self.paper_objects.append(obj2)
            self.paper_IDs.append(self.objects[obj2])
            obj2.setType('Paper')
        elif obj1.getType() == 'Paper' and obj2.getType() == 'Scissors':
            winner = obj2
            self.paper_objects.remove(obj1)
            self.paper_IDs.remove(self.objects[obj1])
            self.scissors_objects.append(obj1)
            self.scissors_IDs.append(self.objects[obj1])
            obj1.setType('Scissors')
        elif obj1.getType() == 'Scissors' and obj2.getType() == 'Rock':
            winner = obj2
            self.scissors_objects.remove(obj1)
            self.scissors_IDs.remove(self.objects[obj1])
            self.rock_objects.append(obj1)
            self.rock_IDs.append(self.objects[obj1])
            obj1.setType('Rock')
        elif obj1.getType() == 'Scissors' and obj2.getType() == 'Paper':
            winner = obj1
            self.paper_objects.remove(obj2)
            self.paper_IDs.remove(self.objects[obj2])
            self.scissors_objects.append(obj2)
            self.scissors_IDs.append(self.objects[obj2])
            obj2.setType('Scissors')
        else:
            winner = None
        self.canvas_frame.itemconfig(self.objects[obj1], image=obj1.image)
        self.canvas_frame.itemconfig(self.objects[obj2], image=obj2.image)
        self.root.update()
        if winner in self.rock_objects:
            winner_team = self.rock_objects
        elif winner in self.paper_objects:
            winner_team = self.paper_objects
        elif winner in self.scissors_objects:
            winner_team = self.scissors_objects
        else:
            winner_team = []
        if len(winner_team) == len(self.objects):
            self.is_running = False
            if winner_team == self.rock_objects:
                self.winner = 'Rock'
            elif winner_team == self.paper_objects:
                self.winner = 'Paper'
            elif winner_team == self.scissors_objects:
                self.winner = 'Scissors'
            self.endResult()

    def endResult(self):
        """ Creates message box telling user if their guess was correct."""
        if self.user_guess.get() == self.winner:
            messagebox.showinfo('Result', 'Congratulations! You guessed {} and {} won.'
                                .format(self.user_guess.get(), self.winner))
        else:
            messagebox.showinfo('Result', 'You guessed {}, but {} won. Better luck next time!'
                                .format(self.user_guess.get(), self.winner))


if __name__ == '__main__':
    main()
