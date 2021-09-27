from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        # stretch uzatmak demek, yani uzatacağız. Her bir turtle 20 20 ile başlıyor.
        # yatay-len dikey-width'e karşılık geliyor.
        self.shapesize(stretch_wid=5, stretch_len=1)  # outline köşelerin keskinliğini ayarlıyor
        self.penup()
        self.setpos(x=xcor, y=ycor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
