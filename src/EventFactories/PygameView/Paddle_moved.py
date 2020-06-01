class Paddle_moved:
    """
    The Brick_destroyed Event
    Updates the board to the new state of the bvh
    """

    def __init__(self, event):
        """
        :param tree: The BVH holding the bricks
        """
        self.paddle = event.paddle

    def update(self, model):
        model.draw_paddle(self.paddle)
