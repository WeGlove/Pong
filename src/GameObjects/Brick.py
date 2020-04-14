from Engine import Shapes
from Engine.GameObject import GameObject


class Brick(Shapes.factory.get_AAB, GameObject):

    def __init__(self, identifier, position, width, height, hits=1, style=0):
        GameObject.__init__(self, identifier)
        Shapes.factory.get_AAB.__init__(self, position, width, height)
        self.hits = hits
        self.style = style

    def hit(self):
        self.hits -= 1
        return self.is_destroyed()

    def is_destroyed(self):
        return self.hits <= 0

    @staticmethod
    def from_coords(upper_left, lower_right):
        return Brick(upper_left + lower_right-upper_left/2, lower_right[0] - upper_left[0], lower_right[1] - upper_left[1])

    def __str__(self):
        return "Brick: Position: " + str(self.position) + " Width/height: " + str(self.width) + " " + str(self.height) + " Hits: " + str(self.hits)
