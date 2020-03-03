from Events.Brick_destroyed import Brick_destroyed
from Commands.Command import Command


class Add_brick(Command):

    def __init__(self, tree):
        self.tree = tree

    def execute(self, model):
        model.board.bricks = self.tree
        return [Brick_destroyed(self.tree)]
