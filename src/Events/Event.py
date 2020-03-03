from abc import abstractmethod


class Event:

    @abstractmethod
    def update(self, board):
        pass
