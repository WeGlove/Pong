import pygame
from src.Views.View import View


class PygameView(View):

    def __init__(self):
        successes, failures = pygame.init()
        print("{0} successes and {1} failures".format(successes, failures))

        self.screen = pygame.display.set_mode((100, 100))

    def update(self, event):
        pass

    def refresh(self):
        pygame.display.flip()
