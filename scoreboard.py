from turtle import Turtle, Screen

ALLIGNMENT = 'center'
FONT = ('courier new', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self,) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.get_prev_high_score()
        self.sety(265)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            self.write_new_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_prev_high_score(self):
        with open('scorecard.txt', 'r') as f:
            prev_high_score = int(f.read())
        return prev_high_score

    def write_new_high_score(self):
        with open('scorecard.txt', 'w') as f:
            f.write(str(self.high_score))
