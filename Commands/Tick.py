from Commands.Command import Command


class Tick(Command):

    def __init__(self, direction):
        self.direction = direction

    def execute(self, model):
        return model.board.tick(model.speed * model.refresh_rate, self.direction)
