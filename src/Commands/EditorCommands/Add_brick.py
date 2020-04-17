from src.Commands.Command import Command
from src import Commands


class Add_brick(Command):

    def __init__(self, tree):
        self.tree = tree

    def execute(self, model):
        model.board.bricks = self.tree
        return [Commands.factory.Brick_destroyed(self.tree)]
