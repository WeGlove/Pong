from abc import abstractmethod

class Paddle_Element:

    @abstractmethod
    def draw(self, screen, paddle, width, height, width_game, height_game, scale_width, scale_height):
        pass
