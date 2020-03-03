from src.Views import Display_modular
import pygame
from src.Models.Editor import Editor
from src import Board_Loader
import json
from src.Models.Server import Server
from src.Models.Client import Client
from src.Connection import Connection
import threading

with open("Resources\\configuration.json") as config:
    data = json.load(config)
    refresh_rate = 1 / data["refresh_rate"]
    speed = data["speed"]
    path = data["path"]

    while True:
        text = input("Type in a command:")
        if text == "editor":
            connection = Connection()
            board = Board_Loader.Board_Loader.load_board(path + "out.json")
            pygame.font.init()
            display = Display_modular.Display_modular.mono_scheme(0xFF0000, 0x00FF00, 0x0000FF, 0x0FFFF00,
                                                                  pygame.font.SysFont("timesnewroman", 72), 0xFFFF00)

            server = Server(board, connection, refresh_rate=refresh_rate, speed=speed)
            editor = Editor(display, connection)
            threading.Thread(target=server.run).start()
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
            print(f"Command <{text}> not found, try < help >")
