class Brick_destroyed:

    def __init__(self, tree):
        self.tree = tree

    def update(self, board, ball_index, position, direction):
        ball = board.balls[ball_index]
        ball.set_position(position)
        ball.set_direction(direction)
