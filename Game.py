import pygame

class Game:

    LEFT = 0
    NONE = 1
    RIGHT = 2

    def __init__(self, board, refresh_rate=1/60, speed=1.0, display=None):
        self.Board = board
        self.refresh_rate = refresh_rate
        self.speed = speed
        self.display = display

    def run(self):
        import time
        while True:
            before = time.time()
            pygame.event.get()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                break

            self.Board.tick(self.speed*self.refresh_rate, self.get_keyboard_input())
            self.display.update(self.Board)
            now = time.time()
            time.sleep(before - now + self.refresh_rate if before - now + self.refresh_rate > 0 else 0)
            print("Waited", before - now + self.refresh_rate)

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
