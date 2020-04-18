import pygame
from src.Views.View import View
from src.EventFactories.PygameView.PygameFactory import PygameFactory


class PygameView(View):

    def __init__(self):
        successes, failures = pygame.init()
        print(f"{successes} successes and {failures} failures")

        self.screen_width = 1000
        self.screen_height = 1000

        self.camera_width = 500
        self.camera_height = 500

        self.cam_scr_width = self.screen_width / self.camera_width
        self.cam_scr_height = self.screen_height / self.camera_height

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.factory = PygameFactory()

        self.board = None

        self.ball_layer = pygame.Surface((self.screen_width, self.screen_height))
        self.brick_layer = pygame.Surface((self.screen_width, self.screen_height))
        self.background = pygame.Surface((self.screen_width, self.screen_height))

        self.background.fill(0x00FFFFFF)

    def update(self, event):
        event.view_event(self.factory).update(self)

    def draw_ball(self, ball):
        pygame.draw.ellipse(self.ball_layer, 0x00FF0000,
                            pygame.Rect(
                                        ((ball.position[0] - ball.error) * self.cam_scr_width, (ball.position[1] - ball.error) * self.cam_scr_height),
                                        (ball.error * 2 * self.cam_scr_width, ball.error * 2 * self.cam_scr_height)),
                            2)

    def draw_balls(self, balls):
        self.ball_layer.fill(0x00000000)
        self.ball_layer.set_colorkey(0x00000000)
        for ball in balls:
            self.draw_ball(ball)

    def draw_brick(self, brick):
        surf = pygame.Surface((brick.width * self.cam_scr_width, brick.height * self.cam_scr_height))
        surf.fill(0x000000FF)
        self.brick_layer.blit(surf, (brick.position[0] * self.cam_scr_width, brick.position[1] * self.cam_scr_height))

    def draw_bricks(self, bricks):
        self.brick_layer.fill(0x00000000)
        self.brick_layer.set_colorkey(0x00000000)
        for brick in bricks:
            self.draw_brick(brick)

    def refresh(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.brick_layer, (0, 0))
        self.screen.blit(self.ball_layer, (0, 0))
        pygame.display.flip()
        self.ball_layer = pygame.Surface((self.screen_width, self.screen_height))
