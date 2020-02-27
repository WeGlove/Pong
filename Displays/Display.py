from abc import abstractmethod


class Display:

    def __init__(self,  width=800, height=800, width_game=100, height_game=100):
        self.width_game = width_game
        self.height_game = height_game

        self.width = width
        self.height = height

        self.scale_width = 1/(self.width_game-1)*(self.width-1)
        self.scale_height = 1/(self.height_game-1)*(self.height-1)

    @abstractmethod
    def update(self, board):
        pass
