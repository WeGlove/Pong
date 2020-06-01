from abc import abstractmethod


class View:

    @abstractmethod
    def update(self, event):
        pass

    @abstractmethod
    def refresh(self):
        pass

    @abstractmethod
    def clear(self):
        pass
