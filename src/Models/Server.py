from Events import Board_set


class Server:

    def __init__(self, board, connection, refresh_rate=1/60, speed=1.0):
        self.board = board
        self.refresh_rate = refresh_rate
        self.speed = speed
        self.connection = connection
        self.paused = False

    def run(self):
        self.connection.push_to_clients([Board_set.Board_set(self.board)])
        print("Server: Sent Board")
        self.__tick_loop()

    def __tick_loop(self):
        import time
        while True:
            before = time.time()

            self.connection.server_wait_for_msg()
            while not self.connection.server_has_events():
                pass
            print("Server: Received direction")

            self.connection.push_to_clients(self.connection.pop_server()[0].execute(self))
            print("Server: Sent updates")
            now = time.time()
            time.sleep(before - now + self.refresh_rate if before - now + self.refresh_rate > 0 else 0)
            print("Waited", before - now + self.refresh_rate)

