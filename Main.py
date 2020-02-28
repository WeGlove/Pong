from Displays import Display_modular
import pygame
import Editor
import Board_Loader
from Board import Board as Test
import json
from Game import Game
from Displays.DisplayElements.Brick_Elements.Brick_Element_Polygon import Brick_Element_Polygon as Poly
from Server import Server
from Client import Client
from Connection import Connection
import threading

with open("configuration.json") as config:
    data = json.load(config)
    refresh_rate = 1 / data["refresh_rate"]
    speed = data["speed"]
    path = data["path"]

    while True:
        text = input("Type in a command:")
        if text == "editor":
            pygame.font.init()
            display = Display_modular.Display_modular.mono_scheme(0xFF0000, 0x00FF00, 0x0000FF, 0x0FFFF00,
                                                                  pygame.font.SysFont("timesnewroman", 72), 0xFFFF00)
            editor = Editor.Editor(display, refresh_rate=refresh_rate)
            editor.run()
        elif text == "game":
            connection = Connection()
            board = Board_Loader.Board_Loader.load_board(path + "out.json")
            pygame.font.init()
            display = Display_modular.Display_modular.mono_scheme(0xFF0000, 0x00FF00, 0x0000FF, 0x0FFFF00,
                                                                  pygame.font.SysFont("timesnewroman", 72), 0xFFFF00)

            server = Server(board, connection, refresh_rate=refresh_rate, speed=speed)
            client = Client(display, connection)
            threading.Thread(target=server.run).start()
            client.run()
        elif text == "help":
            print("Available Commands: editor, help, game, exit")
        elif text == "exit":
            print("Good Night")
            break
        else:
            print("Command <", text, "> not found, try < help >")
