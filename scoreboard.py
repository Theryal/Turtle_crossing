from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 1

    def update_scoring(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def scoring_point(self):
        self.level += 1
        self.update_scoring()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)