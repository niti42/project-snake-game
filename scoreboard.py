from turtle import Turtle, Screen

ALLIGNMENT = 'center'
FONT = ('courier new', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self,) -> None:
        super().__init__()
        self.score = 0
        self.sety(265)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.sety(0)
        self.write(f"Game Over", align=ALLIGNMENT, font=FONT)
