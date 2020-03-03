import pygame
from Commands.Tick import Tick

class Client:

    LEFT = 0
    NONE = 1
    RIGHT = 2

    def __init__(self, display, connection):
        self.display = display
        self.connection = connection
        self.board = None

    def run(self):
        self.connection.client_wait_for_msg()
        print("Client: Received Board")
        self.board = self.connection.pop_clients()[0].board
        while True:
            pygame.event.get()
            self.connection.push_to_server([Tick(self.get_keyboard_input())])
            print("Client: Sent direction")
            while not self.connection.clients_have_events():
                pass
            print("Client: Received Updates")
            for event in self.connection.pop_clients():
                event.update(self)
            self.display.update(self.board)

    def get_keyboard_input(self):

        pressed = pygame.key.get_pressed()
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        if left and right or not left and not right:
            return self.NONE
        else:
            if left:
                return self.LEFT
            else:
                return self.RIGHT
