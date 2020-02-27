from Simples.Simple import Simple
import numpy
import Intersection


class AABB(Simple):

    def __init__(self, position, width, height):
        self.position = position

        self.width = width
        self.height = height

        self.up = position[1] + height / 2  # Assumes the canon COS
        self.down = position[1] - height / 2

        self.right = position[0] + width / 2
        self.left = position[0] - width / 2

    def set_position(self, position):
        self.position = position

        self.up = position[1] + self.height / 2
        self.down = position[1] - self.height / 2

        self.right = position[0] + self.width / 2
        self.left = position[0] - self.width / 2

    def intersect(self, ray, parents=None):
        up = self.up + ray.error
        down = self.down - ray.error

        left = self.left - ray.error
        right = self.right + ray.error

        if ray.direction[0] == 0:
            if ray.direction[1] == 0:
                if down <= ray.position[1] <= up and left <= ray.position[0] <= right:
                    return [Intersection.Intersection(0, numpy.array([0,0]), self, parents),
                            Intersection.Intersection(0, numpy.array([0,0]), self, parents)]
                else:
                    return []
            else:
                t0y = (down - ray.position[1]) / ray.direction[1]
                t1y = (up - ray.position[1]) / ray.direction[1]
                if left <= ray.position[0] <= right:
                    return [Intersection.Intersection(t0y, numpy.array([0, -1]), self, parents),
                            Intersection.Intersection(t1y, numpy.array([0, 1]), self, parents)] \
                            if t0y < t1y else \
                           [Intersection.Intersection(t1y, numpy.array([0, 1]), self, parents),
                            Intersection.Intersection(t0y, numpy.array([0, -1]), self, parents)]
                else:
                    return []
        else:
            if ray.direction[1] == 0:
                t0x = (left - ray.position[0]) / ray.direction[0]
                t1x = (right - ray.position[0]) / ray.direction[0]
                if left <= ray.position[0] <= right:
                    return [Intersection.Intersection(t0x, numpy.array([-1, 0]), self, parents),
                            Intersection.Intersection(t1x, numpy.array([1, 0]), self, parents)] \
                            if t0x < t1x else \
                           [Intersection.Intersection(t1x, numpy.array([1, 0]), self, parents),
                            Intersection.Intersection(t0x, numpy.array([-1, 0]), self, parents)]
                else:
                    return []

        tLeft = (left - ray.position[0]) / ray.direction[0]
        tRight = (right - ray.position[0]) / ray.direction[0]
        if tLeft > tRight:
            tLeft, tRight = tRight, tLeft

        tUp = (up - ray.position[1]) / ray.direction[1]
        tDown = (down - ray.position[1]) / ray.direction[1]
        if tDown > tUp:
            tDown, tUp = tUp, tDown

        if tLeft > tUp or tDown > tRight:
            return []
        else:
            intersections = []
            if tDown > tLeft:
                tMin = tDown
                normalMin = numpy.array([0,-1])
            else:
                tMin = tLeft
                normalMin = numpy.array([-1,0])

            if tUp < tRight:
                tMax = tUp
                normalMax = numpy.array([0,1])
            else:
                tMax = tRight
                normalMax = numpy.array([1,0])

            if tMin > tMax:
                tMin, tMax = tMax, tMin
                normalMin, normalMax = normalMax, normalMin
            intersections.extend([Intersection.Intersection(tMin, normalMin, self, parents),
                                  Intersection.Intersection(tMax, normalMax, self, parents)])
            return intersections

    def is_in(self, point):
        return self.position[0] - self.width / 2 <= point[0] <= self.position[0] + self.width / 2 and \
               self.position[1] - self.height / 2 <= point[1] <= self.position[1] + self.height / 2

    def get_bounding_box(self):
        return AABB(self.position, self.width, self.height)

    def to_coordinates(self):
        """
        Returns a coordinate representation of the Box
        It holds that left <= right and down <= up
        :return:
        """
        return numpy.array([self.left, self.down]), numpy.array([self.right, self.up])

    @staticmethod
    def from_coordinates(down_left, up_right):
        position = down_left + (up_right - down_left) / 2
        return AABB(position, abs(up_right[0] - down_left[0]), abs(up_right[1] - down_left[1]))