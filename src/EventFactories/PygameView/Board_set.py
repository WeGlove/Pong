class Board_set:
    """
    The Boards set event is meant to set up the playing field and thus only contains a board and no update function
    """

    def __init__(self, event):
        self.board = event.board

    def update(self, model):
        model.board = self.board
        model.draw_balls()
        model.draw_bricks(self.board.bricks.get_leaves())
