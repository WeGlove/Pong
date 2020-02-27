from Ray import Ray
import numpy

class Ball(Ray):

    def __init__(self, position, velocity, radius=0):
        Ray.__init__(self, position, velocity, radius)

    def __str__(self):
        return "Ball:\n\t\tPosition:" + str(self.position) + " Velocity: " + str(self.direction)

    def to_json(self):
        return {"position": [int(self.position[0]), int(self.position[1])],
                "velocity": [int(self.direction[0]), int(self.direction[1])],
                "radius": self.error,
                }

    @staticmethod
    def from_json(data):
        return Ball(numpy.array(data["position"]), numpy.array(data["velocity"]), data["radius"])
