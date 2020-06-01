import pygame
from src.Views.View import View
from src.EventFactories.PygameView.PygameFactory import PygameFactory
import numpy
from Engine.Camera import Camera


class PygameView(View):

    BLACK = 0x00000000

    def __init__(self):
        successes, failures = pygame.init()
        print(f"{successes} successes and {failures} failures")

        self.screen_width = 1000
        self.screen_height = 1000

        self.camera = Camera(numpy.array([100, 100]), width=200, height=200,
                             identifier=1, resolution_x=1000, resolution_y=1000)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong")
        self.factory = PygameFactory()

        self.board = None

        self.font = pygame.font.SysFont("code", 16)

        self.background = pygame.Surface((self.camera.resolution_x, self.camera.resolution_y))
        self.full = pygame.Surface((self.camera.resolution_x, self.camera.resolution_y))
        self.brick_layer = pygame.Surface((self.camera.resolution_x, self.camera.resolution_y))
        self.brick_layer.fill(0x00000000)
        self.brick_layer.set_colorkey(0x00000000)

        self.background.fill(0x00FFFFFF)

    def update(self, event):
        event.view_event(self.factory).update(self)

    def draw_ball(self, ball):
        camera_pos = self.camera.world_to_cam(ball.position)
        radius_x = self.camera.world_to_cam_scale_x(ball.error)
        radius_y = self.camera.world_to_cam_scale_y(ball.error)
        pygame.draw.ellipse(self.full, 0x00FF0000,
                            pygame.Rect(
                                        (camera_pos[0] - radius_x,
                                         camera_pos[1] - radius_y),
                                        (radius_x * 2, radius_y * 2)),
                                        1
                            )

    def draw_balls(self, balls):
        for ball in balls:
            self.draw_ball(ball)

    def draw_brick(self, brick):
        surf = pygame.Surface((self.camera.world_to_cam_scale_x(brick.width), self.camera.world_to_cam_scale_y(brick.height)))
        surf.fill(0x000000FF)
        camera_pos = self.camera.world_to_cam(brick.position)
        self.brick_layer.blit(surf, (camera_pos[0] - self.camera.world_to_cam_scale_x(brick.width/2),
                                     camera_pos[1] - self.camera.world_to_cam_scale_y(brick.height/2)))
        text = self.font.render(f"{brick.identifier}", True, (0, 128, 0))
        text = pygame.transform.flip(text, False, True)
        self.brick_layer.blit(text, (camera_pos[0],
                                     camera_pos[1] - self.camera.world_to_cam_scale_y(brick.height/2)))

    def draw_paddle(self, paddle):
        surf = pygame.Surface((self.camera.world_to_cam_scale_x(paddle.width),
                               self.camera.world_to_cam_scale_y(paddle.height)))
        surf.fill(0x00FF0000)
        camera_pos = self.camera.world_to_cam(paddle.position)
        self.full.blit(surf, (camera_pos[0] - self.camera.world_to_cam_scale_x(paddle.width/2),
                                      camera_pos[1] - self.camera.world_to_cam_scale_y(paddle.height/2)))

    def draw_bricks(self, bricks):
        self.brick_layer.fill(self.BLACK)
        for brick in bricks:
            self.draw_brick(brick)
        self.full.blit(self.brick_layer, (0, 0))

    def undraw_bricks(self, bricks):
        for brick in bricks:
            self.undraw_brick(brick)
        self.full.blit(self.brick_layer, (0, 0))

    def undraw_brick(self, brick):
        surf = pygame.Surface((self.camera.world_to_cam_scale_x(brick.width), self.camera.world_to_cam_scale_y(brick.height)))
        surf.fill(0x00111111)
        camera_pos = self.camera.world_to_cam(brick.position)
        self.brick_layer.blit(surf, (camera_pos[0] - self.camera.world_to_cam_scale_x(brick.width/2),
                                     camera_pos[1] - self.camera.world_to_cam_scale_y(brick.height/2)))

    def refresh(self):
        out = pygame.transform.flip(self.full, False, True)
        pygame.transform.scale(out, (self.screen_width, self.screen_height), self.screen)
        pygame.display.flip()

    def clear(self):
        pass
