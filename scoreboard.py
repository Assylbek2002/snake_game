from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_file())
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align='Center', font=('Courier', 15, 'normal'))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align='Center', font=('Courier', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    @staticmethod
    def read_file():
        with open("data.txt") as file:
            contents = file.read()
        return contents

    @staticmethod
    def write_file(new_value):
        with open("data.txt", mode="w") as file:
            file.write(str(new_value))
