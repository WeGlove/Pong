from Simples.AABB import AABB
import numpy
import math


class Rectangle(AABB):

    def __init__(self, position, width, height, angle):
        AABB.__init__(self, position, width, height)

        self.angle = angle

        self.trans_matrix = numpy.array([math.cos(-self.angle), -math.sin(-self.angle)],
                                        [math.sin(self.angle), math.cos(self.angle)]
                                        )

    def set_angle(self, angle):
        self.angle = angle
        self.trans_matrix = numpy.array([math.cos(-self.angle), -math.sin(-self.angle)],
                                        [math.sin(self.angle), math.cos(self.angle)]
                                        )

    def intersect(self, ray, parents=None):
        ray_copy = ray.copy()
        return super().intersect(ray_copy, parents)
