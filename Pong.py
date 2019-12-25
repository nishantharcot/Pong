import turtle

Window = turtle.Screen()
Window.title("Pong by Nishanth")
Window.bgcolor("Black")
Window.setup(width = 800, height = 600)
Window.tracer(0)

# Paddle_A

paddle_a = turtle.Turtle()
# speed is speed of animation, sets the speed to max possible speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

# Paddle_B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Game Functions

def paddle_a_Up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_a_Down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_Up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_b_Down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

# Keyboard Binding

Window.listen()

# Paddle_A

Window.onkeypress(paddle_a_Up, "w")
Window.onkeypress(paddle_a_Down, "s")

# Paddle_B

Window.onkeypress(paddle_b_Up, "Up")
Window.onkeypress(paddle_b_Down, "Down")

# Main Game Loop
while True:
    Window.update()
