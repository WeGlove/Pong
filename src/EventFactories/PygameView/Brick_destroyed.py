class Brick_destroyed:
    """
    The Brick_destroyed Event
    Updates the board to the new state of the bvh
    """

    def __init__(self, event):
        """
        :param tree: The BVH holding the bricks
        """
        self.brick = event.brick

    def update(self, model):
        model.undraw_bricks([self.brick])
        overlaps = model.board.bricks.overlaps(self.brick.get_bounding_box())
        model.draw_bricks(overlaps)
