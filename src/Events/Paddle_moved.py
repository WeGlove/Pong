from Events.Event import Event


class Paddle_moved(Event):
    """
    The Brick_destroyed Event
    Updates the board to the new state of the bvh
    """

    def __init__(self, paddle):
        """
        :param tree: The BVH holding the bricks
        """
        self.paddle = paddle

    def update(self, model):
        model.board.paddle = self.paddle
