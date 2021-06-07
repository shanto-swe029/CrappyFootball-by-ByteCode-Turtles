import turtle
import os


#The window and input names
window = turtle.Screen()
window.title("Crappy Footfootball")
#window.bgcolor("black") #Chobi load na hoile
screen_width = 800
screen_length = 600
window.setup(screen_width, screen_length)
window.bgpic("CrpF.png")
Goalkeeper_1= window.textinput("Goalkeeper_1", " First player : ")
Goalkeeper_2=window.textinput("Goalkeeper_2", " Second player : ")
window.tracer(0)  #Keeps window from updating so main loop e nijera korbo.
window.bgpic("bg.png")


#Score
score_G1 = 0
score_G2 = 0


# Football, The Ball
football = turtle.Turtle()
football.speed(9)
window.addshape('ballp.gif')
football.shape('ballp.gif')
#football.color("white")
football.penup()
football.goto(0, 0)
football.dx = 2
football.dy = 2


#Showing Scores
show_scores = turtle.Turtle()
show_scores.speed(9)
show_scores.shape("square")
show_scores.color("white")
show_scores.penup()
show_scores.hideturtle()
show_scores.goto(0, 240)
show_scores.write("Get Ready, {} , {} ".format(Goalkeeper_1, Goalkeeper_2), align='center', font=('Courier', 24, 'bold'))


#GOALKEEPER 1
goalKeeper_1 = turtle.Turtle()
goalKeeper_1.speed(9)
goalKeeper_1.shape("square")
goalKeeper_1.color("brown")
goalKeeper_1.shapesize(stretch_wid=5.5,stretch_len=0.8)
goalKeeper_1.penup()
goalKeeper_1.goto(-350, 0)


#GOALKEEPER 2
goalKeeper_2 = turtle.Turtle()
goalKeeper_2.speed(9)
goalKeeper_2.shape("square")
goalKeeper_2.color("blue")
goalKeeper_2.shapesize(stretch_wid=5.5,stretch_len=0.8)
goalKeeper_2.penup()
goalKeeper_2.goto(350, 0)


# Functions
def goalKeeper_1_up():
    y = goalKeeper_1.ycor()
    y += 35
    goalKeeper_1.sety(y)

def goalKeeper_1_dowindow():
    y = goalKeeper_1.ycor()
    y -= 35
    goalKeeper_1.sety(y)

def goalKeeper_2_up():
    y = goalKeeper_2.ycor()
    y += 35
    goalKeeper_2.sety(y)

def goalKeeper_2_dowindow():
    y = goalKeeper_2.ycor()
    y -= 35
    goalKeeper_2.sety(y)


# Keyboard bindings
window.listen()
window.onkeypress(goalKeeper_1_up, "w")
window.onkeypress(goalKeeper_1_dowindow, "s")
window.onkeypress(goalKeeper_2_up, "Up")
window.onkeypress(goalKeeper_2_dowindow, "Down")


# Game loop
while True:
    window.update()

    # Move the football
    football.setx(football.xcor() + football.dx)
    football.sety(football.ycor() + football.dy)

    # Border checking

    # Top and bottom
    if football.ycor() > 260:
        football.sety(260)
        football.dy *= -1
        os.system("afplay Jump.wav&")

    elif football.ycor() < -260:
        football.sety(-260)
        football.dy *= -1
        os.system("afplay Jump.wav&")

    # Left and right
    if football.xcor() > 380:
        score_G1 += 1
        show_scores.write(" {} : {}  VS {} : {} ".format(Goalkeeper_1, score_G1, Goalkeeper_2, score_G2), align='center', font=('Courier', 24, 'bold'))
        football.goto(0, 0)
        football.dx *= -1

    elif football.xcor() < -380:
        score_G2 += 1
        show_scores.write(" {} : {}  VS {} : {} ".format(Goalkeeper_1, score_G1, Goalkeeper_2, score_G2), align='center', font=('Courier', 24, 'bold'))
        football.goto(0, 0)
        football.dx *= -1

    # Paddle and football collisions
    if football.xcor() < -340 and football.ycor() < goalKeeper_1.ycor() + 40 and football.ycor() > goalKeeper_1.ycor() - 40:
        football.dx *= -1
        os.system("afplay Jump.wav&")

    elif football.xcor() > 340 and football.ycor() < goalKeeper_2.ycor() + 40 and football.ycor() > goalKeeper_2.ycor() - 40:
        football.dx *= -1
        os.system("afplay Jump.wav&")
