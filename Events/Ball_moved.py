class Ball_moved:
    """
    The Ball moved Event updates the balls in the board
    """

    def __init__(self, balls):
        self.balls = balls

    def update(self, board):
        board.balls = self.balls
