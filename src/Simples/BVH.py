from Simples.Group import Group
from src import Ray
import numpy


class BVH(Group):

    SPLIT = 2

    def __init__(self, simples):
        Group.__init__(self, simples)

    def divide(self):
        elements = self.get_leaves()
        if len(self.simples) < self.SPLIT:
            return

        horizontal = True
        if self.bounding_box.width > self.bounding_box.height:
            direction = numpy.array([0, 1])
            horizontal = False
        else:
            direction = numpy.array([1, 0])
        ray = Ray.Ray(self.bounding_box.position, direction)

        left_elements = []
        right_elements = []
        self.simples = []

        for element in elements:
            intersections = element.intersect(ray)
            if not len(intersections) == 0:
                self.simples.append(element)
            else:
                if element.position[1 if horizontal else 0] > self.bounding_box.position[1 if horizontal else 0]:
                    right_elements.append(element)
                else:
                    left_elements.append(element)

        if len(left_elements) < self.SPLIT:
            left = left_elements
        else:
            left = [BVH(left_elements)]
            left[0].divide()

        self.simples.extend(left)

        if len(right_elements) < self.SPLIT:
            right = right_elements
        else:
            right = [BVH(right_elements)]
            right[0].divide()

        self.simples.extend(right)
