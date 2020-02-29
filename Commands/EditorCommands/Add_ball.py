from Events.Ball_moved import Ball_moved
from Commands.Command import Command


class Add_ball(Command):

    def __init__(self, balls):
        self.balls = balls

    def execute(self, model):
        model.board.balls = self.balls
        return [Ball_moved(self.balls)]
