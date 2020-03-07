from src.Simples.Simple import Simple
from src.Simples.AABB import AABB
import numpy


class Group(Simple):

    def __init__(self, simples):
        Simple.__init__(self)
        self.simples = simples
        self.bounding_box = self.create_bounding_box()
        self.hasRefreshed = True

    def intersect(self, ray, parents=None):
        intersections = []
        if parents is None:
            parents = []
        for simple in self.simples:
            parents_copy = parents.copy()
            parents_copy.append(self)
            intersections.extend(simple.intersect(ray, parents_copy))
        return intersections

    def is_in(self, point):
        for simple in self.simples:
            if simple.is_in(point):
                return True
        return False

    def get_bounding_box(self):
        if not self.hasRefreshed:
            self.bounding_box = self.create_bounding_box()
        return self.bounding_box

    def add_simple(self, simple):
        self.simples.append(simple)
        self.hasRefreshed = False

    def remove_simple(self, simple):
        self.simples.remove(simple)

    def get_leaves(self):
        leaves = []
        for simple in self.simples:
            leaves.extend(simple.get_leaves())
        return leaves

    def get_children(self):
        return self.simples

    def get_nodes(self):
        nodes = []
        for simple in self.simples:
            nodes.extend(simple.get_nodes())
            nodes.append(self)
        return nodes

    def create_bounding_box(self):
        down_left = None
        up_right = None

        for simple in self.simples:
            box = simple.get_bounding_box()
            a, b = box.to_coordinates()
            if down_left is None:
                down_left = a
            else:
                if down_left[0] > a[0]:
                    down_left[0] = a[0]
                if down_left[1] > a[1]:
                    down_left[1] = a[1]

            if up_right is None:
                up_right = b
            else:
                if up_right[0] < b[0]:
                    up_right[0] = b[0]
                if up_right[1] < b[1]:
                    up_right[1] = b[1]

        return AABB(numpy.array([0,0]),0,0) if down_left is None else AABB.from_coordinates(down_left, up_right)

