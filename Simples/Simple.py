from abc import abstractmethod

class Simple:

    @abstractmethod
    def intersect(self, ray, parents=None):
        pass

    @abstractmethod
    def is_in(self, point):
        pass

    @abstractmethod
    def get_bounding_box(self):
        pass

    def get_leaves(self):
        return [self]

    def get_children(self):
        return [self]

    def get_nodes(self):
        return [self]
