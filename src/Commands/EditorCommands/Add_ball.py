from src.Commands.Command import Command
from src import Commands


class Add_ball(Command):

    def __init__(self, balls):
        self.balls = balls

    def execute(self, model):
        model.board.balls = self.balls
        return [Commands.factory.Ball_moved(self.balls)]
