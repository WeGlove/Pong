class Client:

    def __init__(self, display, connection):
        self.display = display
        self.connection = connection
        self.board = None

    def run(self):
        while not self.connection.clients_have_events():
            pass
        print("Client: Received Board")
        self.board = self.connection.pop_clients()[0].board
        while True:
            self.connection.push_to_server([1])
            print("Client: Sent direction")
            while not self.connection.clients_have_events():
                pass
            print("Client: Received Updates")
            for event in self.connection.pop_clients():
                event.update(self.board)
            self.display.update(self.board)
