import json
import Board
import Ball
import Brick
import Wall
import Paddle

import numpy

class Board_Loader:

    @staticmethod
    def load_board(filename):
        with open(filename) as json_file:
            data = json.load(json_file)

            board_dimensions = data["Board"]

            balls = []
            for ball in data["Balls"]:
                balls.append(Ball.Ball.from_json(ball))

            paddle = Paddle.Paddle.from_json(data["Paddle"])

            bricks_data = data["Bricks"]
            bricks = []
            for brick_data in bricks_data:
                brick_dimensions = brick_data["dimensions"]
                bricks.append(Brick.Brick(brick_data["position"], brick_dimensions[0], brick_dimensions[1], brick_data["hits"]))

            walls_data = data["Walls"]
            for wall_data in walls_data:
                wall_dimensions = wall_data["dimensions"]
                bricks.append(Wall.Wall(wall_data["position"], wall_dimensions[0], wall_dimensions[1]))

            board = Board.Board(board_dimensions[0], board_dimensions[1], paddle=paddle, balls=balls, bricks=bricks)

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
                hull["Bricks"].append({"position": [int(pos) for pos in brick.position], "dimensions": [brick.width, brick.height], "hits": brick.hits})
            else:
                hull["Walls"].append({"position": [int(pos) for pos in brick.position], "dimensions": [brick.width, brick.height]})

        with open(filename, "w") as file:
            json.dump(hull, file, indent=2)
