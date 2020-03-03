from Events.Event import Event


class Paddle_set(Event):

    def __init__(self, paddle):
        self.paddle = paddle

    def update(self, model):
        model.board.paddle = self.paddle
