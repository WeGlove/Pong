from src.Commands.Command import Command
from src import Commands


class Remove_brick(Command):

    def __init__(self, brick):
        self.brick = brick

    def execute(self, model):
        model.board.bricks.remove_simple(self.brick)
        return [Commands.factory.Brick_destroyed(self.brick)]