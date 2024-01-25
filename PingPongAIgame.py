import turtle
import random


#main window

win = turtle.Screen()  # This line creates a Turtle graphics screen object named win
win.title("Ping Pong Game") # Sets the title of the window to Ping Pong Game.
win.bgcolor("purple")   # win screen sets to light blue
win.setup(width=600, height=400)  # sets win screen widhth and height

# Create the paddles
paddle_a = turtle.Turtle() # creates a new Turtle object named paddle_a
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")    # paddle color black
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250,0)  # paddle_a ki position most left mai dena chahte hain and center mai wrt to x axis

# UI of AI paddle
paddle_b = turtle.Turtle() # create function
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250,0)  # paddle_b ki position most right mai dena chahte hain and center mai wrt to x axis

# Create ball

ball= turtle.Turtle() # create an object ball
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)  # ball in center in win screen
# ball.dx = 3 and ball.dy = 3 are setting the initial speed and direction of a ball
ball.dx = 3  # ball move in x-axis with speed of 3 pixels
ball.dy = 3  # ball move in y-axis with speed of 3 pixels


# Create ScoreBoard
score_a = 0
score_b = 0
scoreboard= turtle.Turtle() # create object scoreboard
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup() # used to lift the turtle / pen
scoreboard.hideturtle()
scoreboard.goto(0,150) # 150 means wrt y axis sb se upr hoga
scoreboard.write(f"YOU: {score_a}           AI: {score_b}", align="center", font=('arial',15,"normal"))

# Move the paddles

def paddle_a_up():
    y = paddle_a.ycor()   # human wala paddle wrt y cordinate 10 pixels up move kre ga
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()    # human wala paddle wrt y cordinate 10 pixels down move kre ga
    y -= 20
    paddle_a.sety(y)       # Set the new y-coordinate for the paddle_a

# paddle_b --> AI paddle
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)        # Set the new y-coordinate for the paddle_b


# AI Control for paddle_b
# Paddle_b wrt ball apni postion change kre ga kio k wo AI Hai
def move_paddle_b():
    if ball.dx > 0:   # This condition checks whether the ball is moving to the right
        if ball.ycor() > paddle_b.ycor() and abs(ball.ycor() - paddle_b.ycor()) > 10:  #  agr ball 10 pixels upr hai AI wale paddle se to AI paddle wrt y cordinate 20 pixel up apni place change kre
            paddle_b.sety(paddle_b.ycor() + 20)
        if ball.ycor() < paddle_b.ycor() and abs(ball.ycor() - paddle_b.ycor()) > 10:  #  agr ball 10 pixels niche hai AI wale paddle se to AI paddle wrt y cordinate 20 pixel down apni place change kre
            paddle_b.sety(paddle_b.ycor() - 20)



# listen tb use krta hai tk key/button click krna ho
win.listen()
win.onkeypress(paddle_a_up , "W" )
win.onkeypress(paddle_a_down , "S" )

# win screen generate hoti rhy
while True:
    win.update() # update the display window

    # for ball move in x-axis
    ball.setx(ball.xcor() + ball.dx)  #sety and setx used to set the X and Y coordinates

    # for ball move in y-axis
    ball.sety(ball.ycor() + ball.dy)

    # Move the AI paddle
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        move_paddle_b()

    if paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()

    # Ball collide with Top and Bottom
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1   # mtlb agr ball top ya bottom se collide hogi to reverse ho jae gi

    # Ball collide with right and score of Human increases
    if ball.xcor() > 290:
        # mtlb agr left ya right pr tkrae to points brh jae and ball phr se center m ajae
        ball.goto(0, 0)
        ball.dy *= -1
        score_a += 1
        scoreboard.clear()
        scoreboard.write(f"YOU: {score_a}           AI: {score_b}", align="center",
                         font=('arial', 15, "normal"))

    # Ball collide with left and score of AI increases
    if ball.xcor() < -290:
        # mtlb agr left ya right pr tkrae to points brh jae and ball phr se center m ajae
        ball.goto(0, 0)
        ball.dy *= -1
        score_b += 1
        scoreboard.clear()
        scoreboard.write(f"YOU: {score_a}           AI: {score_b}", align="center",
                         font=('arial', 15, "normal"))

        # Check collision with paddle_b
    if ball.xcor() > 240 and ball.xcor() < 250 and (
                ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50): # paddle_b.ycor() + 50 represents the vertical upper limit.
            ball.setx(240)     # This line sets the x-coordinate of the ball to 240
            ball.dx *= -1    # agr ball paddle_b se tkrae gi to reverse ho jae gi

        # Check collision with paddle_a
    if ball.xcor() < -240 and ball.xcor() > -250 and (
                ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-240)
            ball.dx *= -1    # agr ball paddle_a se tkrae gi to reverse ho jae gi

        # jisne pehle 5 score kia wo win ho jae ga
    if score_a == 5 or score_b == 5:
            scoreboard.clear()
            if score_a == 5:
                scoreboard.write("You Win", align="center", font=("arial", 14, "bold"))
            if score_b == 5:
                scoreboard.write("AI WIN", align="center", font=("arial", 14, "bold"))
            break

win.mainloop()
