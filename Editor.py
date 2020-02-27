import pygame
import Board
import Brick
import Wall
import Ball
import numpy
import Paddle
import Board_Loader

class Editor:

    def __init__(self, display, refresh_rate=1/60):
        width = int(input("Please give the width of your game"))
        height = int(input("Please give the height of your game"))
        self.display = display
        self.refresh_rate = refresh_rate
        self.board = Board.Board(width, height, bricks=[])
        self.pressed_left = False
        self.pressed_middle = False
        self.pressed_right = False
        self.selection = 0

    def run(self):
        import time
        while True:
            before = time.time()
            pygame.event.get()

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                break

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_l]:
                self.load(input("Input a filename"))

            if pressed[pygame.K_s]:
                self.save(input("Input a filename"))

            print(pygame.mouse.get_pressed())
            if pygame.mouse.get_pressed()[0] == 1:
                if not self.pressed_left:
                    self.pressed_left = True
                    self.mouse_pressed()
            elif pygame.mouse.get_pressed()[2] == 1:
                if not self.pressed_right:
                    self.pressed_right = True
                    self.mouse_delete()
            else:
                self.pressed_left = False
                self.pressed_right = False
                if pygame.mouse.get_pressed()[1] == 1:
                    if not self.pressed_middle:
                        self.pressed_middle = True
                        self.selection = (self.selection + 1) % 4
                        self.board.bricks_destroyed = self.selection
                else:
                    self.pressed_middle = False

            self.display.update(self.board)
            now = time.time()
            time.sleep(before - now + self.refresh_rate if before - now + self.refresh_rate > 0 else 0)
            #print("Waited", before - now + self.refresh_rate)

    def load(self, filename):
        self.board = Board_Loader.Board_Loader.load_board("C:\\Users\\Tobias\\Desktop\\" + filename)

    def save(self, filename):
        Board_Loader.Board_Loader.save_board(self.board, "C:\\Users\\Tobias\\Desktop\\" + filename)

    def mouse_pressed(self):
        position = pygame.mouse.get_pos()

        x = position[0] / self.display.width * self.board.width
        y = position[1] / self.display.height * self.board.height
        position = numpy.array([x, y])
        if self.selection == 0:
            brick = Brick.Brick(position, 10, 2, hits=1)
            self.board.bricks.add_simple(brick)
        elif self.selection == 1:
            wall = Wall.Wall(position,10,2)
            self.board.bricks.add_simple(wall)
        elif self.selection == 2:
            ball = Ball.Ball(position, numpy.array([1,1]), 2)
            self.board.balls.append(ball)
        elif self.selection == 3:
            paddle = Paddle.Paddle(0, 1, 10, 2, numpy.array([position, position+10]))
            self.board.paddle = paddle

    def mouse_delete(self):
        print("deleting!")
        position = pygame.mouse.get_pos()

        x = position[0] / self.display.width * self.board.width
        y = position[1] / self.display.height * self.board.height
        position = numpy.array([x, y])
        for brick in self.board.bricks.get_children():
            if brick.is_in(position):
                self.board.bricks.remove_simple(brick)


