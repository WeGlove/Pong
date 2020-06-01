from src.EventFactories.Event import Event


class Brick_destroyed(Event):
    """
    The Brick_destroyed Event
    Updates the board to the new state of the bvh
    """

    def __init__(self, brick):
        """
        :param tree: The BVH holding the bricks
        """
        self.brick = brick

    def update(self, model):
        model.board.bricks.delete(hash(self.brick))


    def view_event(self, factory):
        return factory.Brick_destroyed(self)
