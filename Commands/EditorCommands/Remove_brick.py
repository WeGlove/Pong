from Events.Brick_destroyed import Brick_destroyed
from Commands.Command import Command


class Remove_brick(Command):

    def __init__(self, brick):
        self.brick = brick

    def execute(self, model):
        model.board.bricks.remove_simple(self.brick)
        return [Brick_destroyed(self.brick)]