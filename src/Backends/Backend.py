from abc import abstractmethod


class Backend:

    @abstractmethod
    def get_keyboard(self):
        pass

    @abstractmethod
    def get_mouse(self):
        pass

    @abstractmethod
    def get_view(self):
        pass

