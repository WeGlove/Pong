import json
from src.GameObjects.Wall import Wall
from src.GameObjects.Ball import Ball
from src.GameObjects.Paddle import Paddle
from src.GameObjects.Brick import Brick
from src.Board import Board


class Board_Loader:

    @staticmethod
    def load_board(filename):
        with open(filename) as json_file:
            data = json.load(json_file)

            board_dimensions = data["Board"]
            board = Board(board_dimensions[0], board_dimensions[1])

            balls = []
            for ball_data in data["Balls"]:
                next_id = board.game_objects.getNextID()
                ball = Ball.from_json(ball_data, next_id)
                board.game_objects[next_id] = ball
                balls.append(ball)
            board.balls = balls

            next_id = board.game_objects.getNextID()
            paddle = Paddle.from_json(data["Paddle"], next_id)
            board.game_objects[next_id] = paddle

            bricks_data = data["Bricks"]
            bricks = []
            for brick_data in bricks_data:
                next_id = board.game_objects.getNextID()
                brick_dimensions = brick_data["dimensions"]
                brick = Brick(next_id, brick_data["position"], brick_dimensions[0], brick_dimensions[1], brick_data["hits"])
                bricks.append(brick)

            walls_data = data["Walls"]
            for wall_data in walls_data:
                next_id = board.game_objects.getNextID()
                wall_dimensions = wall_data["dimensions"]
                wall = Wall(next_id, wall_data["position"], wall_dimensions[0], wall_dimensions[1])
                bricks.append(wall)

            for brick in bricks:
                board.bricks.add(brick)

            return board

    @staticmethod
    def save_board(board, filename):
        hull = {}
        hull["Board"] = [board.width, board.height]
        hull["Balls"] = [ball.to_json() for ball in board.balls]
        hull["Paddle"] = Paddle.Paddle.to_json(board.paddle)
        hull["Bricks"] = []
        hull["Walls"] = []

        for brick in board.bricks.get_leaves():
            if isinstance(brick, Brick.Brick):
                hull["Bricks"].append(
                    {"position": [int(pos) for pos in brick.position], "dimensions": [brick.width, brick.height],
                     "hits": brick.hits})
            else:
                hull["Walls"].append(
                    {"position": [int(pos) for pos in brick.position], "dimensions": [brick.width, brick.height]})

        with open(filename, "w") as file:
            json.dump(hull, file, indent=2)