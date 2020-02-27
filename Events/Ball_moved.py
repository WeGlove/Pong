class Ball_moved:

    def __init__(self, ball_index, position, direction):
        self.ball_index = ball_index
        self.position = position
        self.direction = direction

    def update(self, board):
        ball = board.balls[self.ball_index]
        ball.set_position(self.position)
        ball.set_direction(self.direction)
