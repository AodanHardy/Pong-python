import turtle as tl

import paddle
from paddle import *

window = tl.Screen()
window.title("Pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

# paddle A
paddle_a = paddle.Paddle(0)


# paddle B
paddle_b = paddle.Paddle(0)


# Ball
ball = tl.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Function

while True:
    window.update()
