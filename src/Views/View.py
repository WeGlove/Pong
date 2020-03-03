from abc import abstractmethod

class View:

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self, event):
        pass
