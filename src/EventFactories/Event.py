from abc import abstractmethod


class Event:

    @abstractmethod
    def update(self, board):
        pass

    @abstractmethod
    def update_view(self, view):
        pass

    @abstractmethod
    def view_event(self, factory):
        pass