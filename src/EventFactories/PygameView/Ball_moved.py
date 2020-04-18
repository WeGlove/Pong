class Ball_moved:
    """
    The Ball moved Event updates the balls in the board
    """

    def __init__(self, event):
        self.balls = event.balls

    def update(self, model):
        model.draw_balls(self.balls)
