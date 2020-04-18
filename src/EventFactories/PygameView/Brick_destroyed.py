class Brick_destroyed:
    """
    The Brick_destroyed Event
    Updates the board to the new state of the bvh
    """

    def __init__(self, event):
        """
        :param tree: The BVH holding the bricks
        """
        self.tree = event.tree

    def update(self, model):
        model.draw_bricks(self.tree.get_leaves())
