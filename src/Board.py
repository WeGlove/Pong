import Engine
Engine.init()
from src.EventFactories.Std import Brick_destroyed, Ball_moved
from src.GameObjects import Brick
from Engine.GameObjectHashMap import GameObjectHashMap


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.balls = []
        self.paddle = None
        self.bricks = Engine.shape_factory.LeastAddition([])
        self.brick_count = 0
        self.game_objects = GameObjectHashMap()

        self.bricks_destroyed = 0

    def tick(self, speed, input):
        events = []
        if self.paddle is not None:
            events.extend([self.paddle.move(input, speed)])
        events.extend(self.move_balls(speed))
        return events

    def move_balls(self, speed):
        remaining_balls = [ball for ball in self.balls]
        speeds = [speed] * len(self.balls)
        intersections = [self.intersect(ball) for ball in self.balls]
        for intersection in intersections:
            print("####")
            for inter in intersection:
                print(inter)
        events = []
        while not len(remaining_balls) == 0:
            print(speeds)
            min = None
            for i in range(len(remaining_balls)):
                if len(intersections[i]) == 0:
                    remaining_balls[i].move(speed)
                    del remaining_balls[i]
                    del speeds[i]
                    del intersections[i]
                    break
                elif intersections[i][0].t > speeds[i] * remaining_balls[i].get_speed():
                    remaining_balls[i].move(speed)
                    del remaining_balls[i]
                    del speeds[i]
                    del intersections[i]
                    break
                else:
                    if min is None:
                        min = i
                    else:
                        min = min if intersections[min][0].t <= intersections[i][0].t else i
            else:
                intersection = intersections[min][0]
                t = intersection.t
                if intersection.intersected.hit():
                    self.bricks.delete(hash(intersection.intersected))
                    events += [Brick_destroyed.Brick_destroyed(intersection.intersected)]
                    self.bricks_destroyed += 1
                    self.brick_count -= 1
                print(remaining_balls[min])
                print(intersection)
                remaining_balls[min].move(t)
                remaining_balls[min].reflect(intersection.normal)
                speeds[min] -= t
                intersections[min] = self.intersect(self.balls[min])
        return events + [Ball_moved.Ball_moved(self.balls)]

    def intersect(self, Ball):
        intersections = self.bricks.intersect(Ball)
        return [inter for inter in self.sort_intersection(intersections) if inter.t >= 0]

    def sort_intersection(self, intersections):
        return sorted(intersections, key=lambda inter: inter.t)

    def to_json(self):
        hull = {}
        hull["Board"] = [self.width, self.height]
        hull["Balls"] = [ball.to_json() for ball in self.balls]
        hull["Paddle"] = self.paddle.to_json()
        hull["Bricks"] = []
        hull["Walls"] = []

        for brick in self.bricks.get_leaves():
            if isinstance(brick, Brick.Brick):
                hull["Bricks"].append({"position": [int(pos) for pos in brick.position], "dimensions": [brick.width, brick.height], "hits": brick.hits})
            else:
                hull["Walls"].append({"position": [int(pos) for pos in brick.position], "dimensions": [brick.width, brick.height]})

        return hull



