class Client:

    def __init__(self, display, connection):
        self.display = display
        self.connection = connection
        self.board = None

    def run(self):
        while True:
            self.display.update(self.board)
