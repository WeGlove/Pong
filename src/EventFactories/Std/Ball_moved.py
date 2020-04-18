from src.EventFactories.Event import Event


class Ball_moved(Event):
    """
    The Ball moved Event updates the balls in the board
    """

    def __init__(self, balls):
        self.balls = balls

    def update(self, model):
        model.board.balls = self.balls

    def view_event(self, factory):
        return factory.Ball_moved(self)
