import turtle as tl


class Paddle:
    startPosition = [0, 0]

    def Paddle(self, x, y):
        self = tl.Turtle()
        self.shape("Square")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

