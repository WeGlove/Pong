from abc import abstractmethod

class Info_Element:

    @abstractmethod
    def draw(self, screen, info, width, height, width_game, height_game, scale_width, scale_height):
        pass
