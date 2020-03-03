import pygame
from src import Ball, Brick, Board, Board_Loader, Paddle, Wall
import numpy

from src.Commands.EditorCommands.Add_brick import Add_brick
from src.Commands.EditorCommands.Add_ball import Add_ball
from src.Commands.EditorCommands.Add_Paddle import Add_Paddle
from src.Commands.EditorCommands.Remove_brick import Remove_brick


class Editor:

    def __init__(self, display, connection, refresh_rate=1/60):
        width = int(input("Please give the width of your game"))
        height = int(input("Please give the height of your game"))
        self.display = display
        self.refresh_rate = refresh_rate
        self.board = Board.Board(width, height, bricks=[])
        self.pressed_left = False
        self.pressed_middle = False
        self.pressed_right = False
        self.selection = 0
        self.connection = connection

    def run(self):
        while not self.connection.clients_have_events():
            pass
        print("Client: Received Board")
        self.board = self.connection.pop_clients()[0].board

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


            if pygame.mouse.get_pressed()[0] == 1:
                if not self.pressed_left:
                    self.pressed_left = True
                    self.connection.push_to_server([self.mouse_pressed()])
            elif pygame.mouse.get_pressed()[2] == 1:
                if not self.pressed_right:
                    self.pressed_right = True
                    self.connection.push_to_server([self.mouse_delete()])
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
            for event in self.connection.pop_clients():
                event.update(self)

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
            return Add_brick(self.board.bricks)
        elif self.selection == 1:
            wall = Wall.Wall(position, 10, 2)
            self.board.bricks.add_simple(wall)
            return Add_brick(self.board.bricks)
        elif self.selection == 2:
            ball = Ball.Ball(position, numpy.array([1, 1]), 2)
            return Add_ball(self.board.balls + [ball])
        elif self.selection == 3:
            paddle = Paddle.Paddle(0, 1, 10, 2, numpy.array([position, position + 10]))
            return Add_Paddle(paddle)

    def mouse_delete(self):
        print("deleting!")
        position = pygame.mouse.get_pos()

        x = position[0] / self.display.width * self.board.width
        y = position[1] / self.display.height * self.board.height
        position = numpy.array([x, y])
        commands = []
        for brick in self.board.bricks.get_children():
            if brick.is_in(position):
                commands.append(Remove_brick(brick))

