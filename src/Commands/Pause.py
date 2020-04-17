from src.Commands.Command import Command


class Pause(Command):

    def __init__(self, setting):
        self.setting = setting

    def execute(self, model):
        model.paused = self.setting
        return []
