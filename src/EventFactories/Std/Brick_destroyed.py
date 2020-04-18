from src.EventFactories.Event import Event


class Brick_destroyed(Event):
    """
    The Brick_destroyed Event
    Updates the board to the new state of the bvh
    """

    def __init__(self, tree):
        """
        :param tree: The BVH holding the bricks
        """
        self.tree = tree

    def update(self, model):
        model.board.bricks = self.tree

    def view_event(self, factory):
        return factory.Brick_destroyed(self)
