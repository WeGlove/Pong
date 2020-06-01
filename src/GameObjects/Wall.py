import Engine
AAB = Engine.shape_factory.AAB


class Wall(AAB):

    def __init__(self, identifier, position, width, height):
        AAB.__init__(self, position, width, height, identifier=identifier)

    def hit(self):
        return False

    def is_destroyed(self):
        return False

    @staticmethod
    def from_coords(upper_left, lower_right):
        return Wall(upper_left + lower_right-upper_left/2, lower_right[0] - upper_left[0], lower_right[1] - upper_left[1])

    def __str__(self):
        return f"Wall: ID: {self.identifier} Position: " + str(self.position) + " Width/height: " + str(self.width) + " " + str(self.height)
