from Events.Paddle_set import Paddle_set
from Commands.Command import Command


class Add_Paddle(Command):

    def __init__(self, paddle):
        self.paddle = paddle

    def execute(self, model):
        return [Paddle_set(self.paddle)]