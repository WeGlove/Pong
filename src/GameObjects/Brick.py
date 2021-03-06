import Engine
AAB = Engine.shape_factory.AAB


class Brick(AAB):

    def __init__(self, identifier, position, width, height, hits=1, style=0):
        AAB.__init__(self, position, width, height, identifier=identifier)
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
        return "Brick: ID:" + str(self.identifier) + " Position: " + str(self.position) + " Width/height: " + str(self.width) + " " + str(self.height) + " Hits: " + str(self.hits)
