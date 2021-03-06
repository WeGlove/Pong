from src.EventFactories.Event import Event


class Paddle_set(Event):

    def __init__(self, paddle):
        self.paddle = paddle

    def update(self, model):
        model.board.paddle = self.paddle

    def view_event(self, factory):
        return factory.Paddle_set(self)
