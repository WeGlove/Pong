import numpy
from Simples.AABB import AABB
from Events.Ball_moved import Ball_moved


class Paddle(AABB):

    def __init__(self, local, velocity, width, height, interval):
        AABB.__init__(self, interval[0]*(1-local) + interval[1]*local, width, height)
        self.velocity = velocity
        self.local = local
        self.interval = interval

    def __str__(self):
        return "Paddle: Position: " + str(self.position) + " Width/height: " + str(self.width) + " " + str(self.height) + " Velocity: " + str(self.velocity)

    def is_destroyed(self):
        return False

    def hit(self):
        return False

    def to_json(self):
        return {"local": self.local,
                "velocity": self.velocity,
                "dimensions": [self.width, self.height],
                "interval": [[int(inter) for inter in self.interval[0]], [int(inter) for inter in self.interval[1]]]
                }

    @staticmethod
    def from_json(data):
        return Paddle(data["local"], data["velocity"], data["dimensions"][0], data["dimensions"][1],
                      numpy.array(data["interval"]))

    def move(self, direction, length):
        if direction == 0:
            new_local = self.local - self.velocity * length
            self.local = new_local if new_local >= 0 else 0

            self.set_position(self.interval[0] * (1-self.local) + self.interval[1] * self.local)

        elif direction == 2:
            new_local = self.local + self.velocity * length
            self.local = new_local if new_local <= 1 else 1

            self.set_position(self.interval[0] * (1-self.local) + self.interval[1] * self.local)

