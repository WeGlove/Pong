from src.EventFactories.Event import Event


class Board_set(Event):
    """
    The Boards set event is meant to set up the playing field and thus only contains a board and no update function
    """

    def __init__(self, board):
        self.board = board

    def update(self, model):
        model.board = self.board

    def view_event(self, factory):
        return factory.Board_set(self)
