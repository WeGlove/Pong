import pygame
from src.Views.Display import Display
from src.Views.DisplayElements.Background_Elements.Background_Mono import Background_Mono
from src.Views.DisplayElements.Ball_Elements.Ball_Mono import Ball_Mono
from src.Views.DisplayElements.Brick_Elements.Brick_Mono import Brick_Mono
from src.Views.DisplayElements.Paddle_Elements.Paddle_Mono import Paddle_Mono
from src.Views.DisplayElements.Info_Elements.Info_Mono import Info_Mono
from src.Views.DisplayElements.BBox_Elements.BBox_Mono import BBox_Mono


class Display_modular(Display):

    def __init__(self, brick, ball, background, paddle, info, bbox, width=800, height=800, width_game=100, height_game=100):
        Display.__init__(self, width, height, width_game, height_game)
        self.ball = ball
        self.brick = brick
        self.background = background
        self.paddle = paddle
        self.info = info
        self.bbox = bbox
        successes, failures = pygame.init()
        print("{0} successes and {1} failures".format(successes, failures))

        self.screen = pygame.display.set_mode((self.width, self.height))

    def update(self, board):
        self.background.draw(self.screen, self.width, self.height, self.width_game, self.height_game, self.scale_width, self.scale_height)
        for brick in board.bricks.get_leaves():
            self.brick.draw(self.screen, brick, self.width, self.height, self.width_game, self.height_game, self.scale_width, self.scale_height)
        if board.paddle is not None:
            self.paddle.draw(self.screen, board.paddle, self.width, self.height, self.width_game, self.height_game, self.scale_width, self.scale_height)
        for ball in board.balls:
            self.ball.draw(self.screen, ball, self.width, self.height, self.width_game, self.height_game, self.scale_width, self.scale_height)
        self.info.draw(self.screen, str(board.bricks_destroyed), self.width, self.height, self.width_game, self.height_game, self.scale_width, self.scale_height)
        for node in board.bricks.get_nodes():
            self.bbox.draw(self.screen, node.get_bounding_box(), self.width, self.height, self.width_game, self.height_game, self.scale_width, self.scale_height)
        pygame.display.flip()


    @staticmethod
    def mono_scheme(brick, ball, background, paddle, info, bbox, width=800, height=800, width_game=100, height_game=100):
        background_element = Background_Mono(background)
        return Display_modular(Brick_Mono(brick), Ball_Mono(ball, background_element), background_element,
                               Paddle_Mono(paddle), Info_Mono(info), BBox_Mono(bbox), width, height, width_game, height_game)
