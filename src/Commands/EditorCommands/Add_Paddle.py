from src.Commands.Command import Command
from src import Commands


class Add_Paddle(Command):

    def __init__(self, paddle):
        self.paddle = paddle

    def execute(self, model):
        return [Commands.factory.Paddle_set(self.paddle)]