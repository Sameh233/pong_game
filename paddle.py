from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True, position = (350,0) ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid= 5,  stretch_len= 1)
        self.goto(position)
        
        
    def up(self):
        if self.ycor() < 260 :
            move_up = self.ycor() + 20
            self.goto(self.xcor(), move_up)
        
    def down(self):
        if self.ycor() > -260 :
            move_down = self.ycor() - 20
            self.goto(self.xcor(), move_down)
            