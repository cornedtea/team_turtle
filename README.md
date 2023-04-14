# **ALERT: THIS REPO IS NO LONGER ACTIVE**
# Rock Paper Scissors
## Team Turtle - Courtney Brown, Alana Nadolski, & Blanche Reading

Repository for COMP 123 final project work

## Project Proposal
Our simulation would create a window containing some number of objects divided into three teams - rock, paper, and scissors. On start, the objects would begin to move around the window at random and, upon colliding with each other, change type depending on who loses. For example, if a ‘scissors’ type collides with a ‘paper’ type, the ‘paper’ type will lose and become a ‘scissors’ type. Movement and collision continue until there is only one team left. We hope to at minimum create a program that will have several objects with random movement within an area and the ability to detect ‘collisions’. We aspire to a program that resembles this. User interaction will be limited to pressing buttons to set up, start, and pause the simulation as well as making a guess as to which team of objects. We don’t yet know how to use the tkinter module, which we will need for the project. 

## Project Design
### User Perspective
After running the program, the user will see a blank canvas with an interface at the top of the window. The interface will contain a “Set up” button, a “Start” button, a “Stop” button, and a label with the object count. The user will be prompted to “Set up” the screen which will cause the program to automatically place the rock, paper, and scissors groups around the screen. Users will then make a prediction based on the objects’ placement of which team will win. The “Start” and “Stop” buttons can be utilized to play and pause the game. The sequence of events will occur as follows: initialize objects via the “Set up” button → user makes guess → user presses the “Start” button → movement and collision start (use of the  “Stop” button is now viable) → objects change “teams” as they collide → only one group remains → movement and collision stop (use of the “Start” and “Stop” buttons is no longer viable) → respond to user guess appropriately. The objects will stop moving when there is only one team left. A popup will appear to notify the user of how their guess measured up to the result.  If the team chosen by the user wins, they get a congratulatory message, otherwise, they get a ‘try again’. The closure of the window is up to the user, and they could run the program again if they wanted to by clicking “Set up” another time. 

### Data Design
Given the use of tkinter, we will be mainly using widgets as objects within the program. Other data, such as widget information, will be stored in lists and dictionaries. Our program will read in 3 images, with one per team. We will create a new class called RockPaperScissors for the program.
