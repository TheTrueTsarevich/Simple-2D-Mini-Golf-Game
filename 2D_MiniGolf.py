## Mini golf 2D version by @TheTrueTsarevich

import turtle
import time


def setup_ball(ball):
    # Drawing the ball
    ball.speed(0)
    ball.penup()
    ball.goto(380, 280)
    ball.pendown()
    ball.color("black", "white")
    ball.begin_fill()
    ball.shape("circle")
    ball.end_fill()
    ball.penup()


def setup_hole(hole):
    # Drawing the hole
    hole.penup()
    hole.speed(0)
    hole.goto(-250, 250)
    hole.pendown()
    hole.color("black")
    hole.begin_fill()
    hole.shape("circle")
    hole.end_fill()
    hole.penup()
    hole.pendown()
    hole.goto(-250, 260)
    hole.penup()


def draw_map():
    # Drawing the borders
    setup = turtle.Turtle()
    setup.color("black", "darkseagreen")
    setup.begin_fill()
    setup.speed(0)
    setup.penup()
    setup.goto(400, 300)
    setup.pendown()
    setup.goto(400, -300)
    setup.goto(-300, -300)
    setup.goto(-300, -50)
    setup.goto(-400, -50)
    setup.goto(-400, 150)
    setup.goto(-300, 150)
    setup.goto(-300, 300)
    setup.goto(-200, 300)
    setup.goto(-200, 200)
    setup.goto(-125, 200)
    setup.goto(-125, 300)
    setup.goto(400, 300)
    setup.penup()
    setup.end_fill()
    setup.hideturtle()


def draw_obstacles():
    # Drawing the obstancles
    setup = turtle.Turtle()
    setup.color("black", "white")
    # Top box
    setup.begin_fill()
    setup.penup()
    setup.speed(0)
    setup.goto(150, 75)
    setup.pendown()
    setup.goto(250, 75)
    setup.goto(250, 175)
    setup.goto(150, 175)
    setup.goto(150, 75)
    setup.penup()
    setup.end_fill()

    # Furthest left
    setup.begin_fill()
    setup.goto(-223, -123)
    setup.pendown()
    setup.goto(-73, -123)
    setup.goto(-73, 0)
    setup.goto(-223, 0)
    setup.goto(-223, -123)
    setup.penup()
    setup.end_fill()

    # Bottom right
    setup.begin_fill()
    setup.goto(300, -50)
    setup.pendown()
    setup.goto(200, -50)
    setup.goto(200, -150)
    setup.goto(300, -150)
    setup.goto(300, -50)
    setup.penup()
    setup.end_fill()
    setup.hideturtle()


def obstacle_collideX(obstaclelist, ball_x, ball_y, x_speed, y_speed):
    # Calculates the collision of the vertical walls of the obstacles
    # Obstacle 1
    if obstaclelist[0][2] <= (ball_y + 10) and (ball_y - 10) <= obstaclelist[0][3] and (ball_x + 13) >= obstaclelist[0][
        0] and (ball_x - 13) <= obstaclelist[0][1]:
        return [-x_speed, y_speed]
    # Obstacle 2
    if obstaclelist[1][2] <= (ball_y + 10) and (ball_y - 10) <= obstaclelist[1][3] and (ball_x + 13) >= obstaclelist[1][
        0] and (ball_x - 13) <= obstaclelist[1][1]:
        return [-x_speed, y_speed]
    # Obstacle 3
    if obstaclelist[2][2] <= (ball_y + 13) and (ball_y - 13) <= obstaclelist[2][3] and (ball_x + 13) >= obstaclelist[2][
        0] and (ball_x - 13) <= obstaclelist[2][1]:
        return [-x_speed, y_speed]
    else:
        return [x_speed, y_speed]


def obstacle_collideY(obstaclelist, ball_x, ball_y, x_speed, y_speed):
    # Calculates the collision of the horizontal walls of the obstacles
    # Obstacle 1
    if obstaclelist[0][0] <= (ball_x + 10) and (ball_x - 10) <= obstaclelist[0][1] and (ball_y + 13) >= obstaclelist[0][
        2] and (ball_y - 13) <= obstaclelist[0][3]:
        print(ball_x, ball_y)
        return [x_speed, -y_speed]
    # Obstacle 2
    if obstaclelist[1][0] <= (ball_x + 10) and (ball_x - 10) <= obstaclelist[1][1] and (ball_y + 13) >= obstaclelist[1][
        2] and (ball_y - 13) <= obstaclelist[1][3]:
        return [x_speed, -y_speed]
    # Obstacle 3
    if obstaclelist[2][0] <= (ball_x + 10) and (ball_x - 10) <= obstaclelist[2][1] and (ball_y + 13) >= obstaclelist[2][
        2] and (ball_y - 13) <= obstaclelist[2][3]:
        return [x_speed, -y_speed]
    else:
        return [x_speed, y_speed]


def boundary_collide(boundarylist, ball_x, ball_y, x_speed, y_speed):
    # Calculates the collision on the course's boundaries
    if boundarylist[0][1] <= ball_y and ball_y <= boundarylist[0][0] and (ball_x + 13) >= boundarylist[1][0]:
        return [-x_speed, y_speed]
    if boundarylist[1][1] <= ball_x and ball_x <= boundarylist[1][0] and (ball_y - 13) <= boundarylist[0][1]:
        return [x_speed, -y_speed]
    if boundarylist[0][1] <= ball_y and ball_y <= boundarylist[0][2] and (ball_x - 13) <= boundarylist[1][1]:
        return [-x_speed, y_speed]
    if boundarylist[1][2] <= ball_x and ball_x <= boundarylist[1][1] and (ball_y - 13) <= boundarylist[0][2]:
        return [x_speed, -y_speed]
    if boundarylist[0][2] <= ball_y and ball_y <= boundarylist[0][3] and (ball_x - 13) <= boundarylist[1][2]:
        return [-x_speed, y_speed]
    if boundarylist[1][2] <= ball_x and ball_x <= boundarylist[1][1] and (ball_y + 13) >= boundarylist[0][3]:
        return [x_speed, -y_speed]
    if boundarylist[0][3] <= ball_y and ball_y <= boundarylist[0][0] and (ball_x - 13) <= boundarylist[1][1]:
        return [-x_speed, y_speed]
    if boundarylist[1][1] <= ball_x and ball_x <= boundarylist[1][3] and (ball_y + 13) >= boundarylist[0][4]:
        return [x_speed, -y_speed]
    if boundarylist[0][5] <= ball_y and ball_y <= boundarylist[0][0] and (ball_x + 13) >= boundarylist[1][3] and (
            ball_x + 13) < boundarylist[1][4]:
        return [-x_speed, y_speed]
    if boundarylist[1][3] <= ball_x and ball_x <= boundarylist[1][4] and (ball_y + 13) >= boundarylist[0][5]:
        return [x_speed, -y_speed]
    if boundarylist[0][5] <= ball_y and ball_y <= boundarylist[0][0] and (ball_x - 13) <= boundarylist[1][4] and (
            ball_x - 13) >= boundarylist[1][3]:
        return [-x_speed, y_speed]
    if boundarylist[1][4] <= ball_x and ball_x <= boundarylist[1][0] and (ball_y + 13) >= boundarylist[0][0]:
        return [x_speed, -y_speed]
    else:
        return [x_speed, y_speed]


def distance_click(ball_x, x2, ball_y, y2):
    # Calculates the distances/power of each shot and scales them if too powerful for the game
    distance = ((x2 - ball_x) ** 2 + (y2 - ball_y) ** 2) ** 0.5
    if distance > 10:
        if abs(x2 - ball_x) > abs(y2 - ball_y):
            distance_x = (x2 - ball_x) * (10 / abs(x2 - ball_x))
            distance_y = (y2 - ball_y) * (10 / abs(x2 - ball_x))
        else:
            distance_x = (x2 - ball_x) * (10 / abs(y2 - ball_y))
            distance_y = (y2 - ball_y) * (10 / abs(y2 - ball_y))
        return [distance_x, distance_y]
    else:
        distance_x = (x2 - ball_x)
        distance_y = (y2 - ball_y)
        return [distance_x, distance_y]


def game_won(ball_x, ball_y):
    # Checks if the game has been won
    if (ball_x - 3.5) <= -250 and (ball_x + 3.5) >= -250 and (ball_y - 3.5) <= 250 and (ball_y + 3.5) >= 250:
        return True
    else:
        return False


def getcoordinates():
    turtle.onscreenclick(click_variable)


def click_variable(x, y):
    # Main function of the whole project with all of the project's contents
    # Is used by the onscreenclick in the turtle module do run almost all the aspects in the game
    global ball_x
    global ball_y
    global attempt

    print("Click where you want to shoot.")

    x2 = x
    y2 = y

    x_speed = distance_click(ball_x, x2, ball_y, y2)[0]
    y_speed = distance_click(ball_x, x2, ball_y, y2)[1]

    # Given the attempts, records how many are laughed and provides a questionable losing splashscreen if the user has lost the game
    attempt = attempt - 1
    if attempt < 0:
        pen.showturtle()
        pen.color("red")
        pen.write("BOZO, L SHOT", align="center", font=("Comic Sans", 72, "normal"))
        time.sleep(0.5)
        pen.color("green")
        pen.write("BOZO, L SHOT", align="center", font=("Comic Sans", 72, "normal"))
        time.sleep(0.5)
        pen.color("blue")
        pen.write("BOZO, L SHOT", align="center", font=("Comic Sans", 72, "normal"))
        pen.write("BOZO, L SHOT", align="center", font=("Comic Sans", 72, "normal"))
        time.sleep(0.5)
        pen.color("green")
        pen.write("BOZO, L SHOT", align="center", font=("Comic Sans", 72, "normal"))
        time.sleep(0.5)
        pen.color("blue")
        pen.write("BOZO, L SHOT", align="center", font=("Comic Sans", 72, "normal"))
        pen.hideturtle()
        hole.clear()
        ball.clear()


    # Checks if the user has won the game
    if game_won(ball_x, ball_y) == True:
        pen.showturtle()
        ball.clear()
        pen.write("CONGRATS, W SHOT.", align="center", font=("Comic Sans", 72, "normal"))
        pen.hideturtle()

    # Ensures that the turtle has an end and isn't going on forever
    if abs(x_speed) <= 0.2 and abs(y_speed) <= 0.2:
        x_speed = 0
        y_speed = 0

    # Main while loop that handles the clicks
    # Has all the collision and point counting systems inside
    while game_won(ball_x, ball_y) == False:
        y_speed = obstacle_collideX(obstaclelist, ball_x, ball_y, x_speed, y_speed)[1] * FRICTION
        x_speed = obstacle_collideX(obstaclelist, ball_x, ball_y, x_speed, y_speed)[0] * FRICTION
        ball_x = ball.xcor() + x_speed
        ball_y = ball.ycor() + y_speed

        y_speed = obstacle_collideY(obstaclelist, ball_x, ball_y, x_speed, y_speed)[1] * FRICTION
        x_speed = obstacle_collideY(obstaclelist, ball_x, ball_y, x_speed, y_speed)[0] * FRICTION
        ball_x = ball.xcor() + x_speed
        ball_y = ball.ycor() + y_speed

        x_speed = boundary_collide(boundarylist, ball_x, ball_y, x_speed, y_speed)[0] * FRICTION
        y_speed = boundary_collide(boundarylist, ball_x, ball_y, x_speed, y_speed)[1] * FRICTION
        ball_x = ball.xcor() + x_speed
        ball_y = ball.ycor() + y_speed
        ball.goto(ball_x, ball_y)

        if game_won(ball_x, ball_y) == True:
            pen.setpos(-400, 0)
            pen.showturtle()
            ball.clear()
            pen.write("CONGRATS, W SHOT.", align="left", font=("Comic Sans", 48, "normal"))
            pen.hideturtle()

# Draws the course
def draw_course():
    draw_map()
    draw_obstacles()

# Intro and definitive lists and other things for the functions to use
attempt = 0
print("Welcome to 2D Mini Golf.")
time.sleep(2)
print("To move the ball, you will click on screen.")
time.sleep(2)
print("What level of difficulty would you like? Easy, Medium, or Hard?")
response = input()
if response == "Hard":
    attempt = 2
elif response == "Medium":
    attempt = 3
else:
    attempt = 5
window = turtle.Screen()
window.setup(800, 500)
draw_course()
ball = turtle.Turtle()
hole = turtle.Turtle()
pen = turtle.Turtle()
pen.hideturtle()
setup_ball(ball)
setup_hole(hole)

ball_x = ball.xcor()
ball_y = ball.ycor()

FRICTION = 0.99

obstaclelist = [[150, 250, 75, 175],
                [200, 300, -150, -50],
                [-223, -73, -123, 0]]

boundarylist = [[300, -300, -50, 150, 300, 200],
                [400, -300, -400, -200, -125]]

# The main magic of the game occurs in the onscreenclick function as well as mainloop
click_coordinates = []
window.onscreenclick(click_variable)
turtle.mainloop()

