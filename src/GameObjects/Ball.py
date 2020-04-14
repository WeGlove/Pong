from Engine.Ray import Ray
import numpy
from Engine.GameObject import GameObject


class Ball(Ray, GameObject):

    def __init__(self, identifier, position, velocity, radius=0):
        GameObject.__init__(self, identifier)
        Ray.__init__(self, position, velocity, radius)

    def __str__(self):
        return f"Ball: Position={self.position} Velocity: {self.direction} Radius={self.error}"

    def to_json(self):
        return {"position": [int(self.position[0]), int(self.position[1])],
                "velocity": [int(self.direction[0]), int(self.direction[1])],
                "radius": self.error,
                }

    @staticmethod
    def from_json(data, identifier):
        return Ball(identifier, numpy.array(data["position"]), numpy.array(data["velocity"]), data["radius"])
