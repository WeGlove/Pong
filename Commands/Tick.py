class Tick:

    def __init__(self, direction):
        self.direction = direction

    def update(self, model):
        return model.board.tick(model.speed * model.refresh_rate, self.direction)
