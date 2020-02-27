from Events import Board_set

class Server:

    def __init__(self, board, connection, refresh_rate=1/60, speed=1.0):
        self.board = board
        self.refresh_rate = refresh_rate
        self.speed = speed
        self.connection = connection

    def run(self):
        self.connection.push_event_client(Board_set.Board_set(self.board))
        self.tick_loop()

    def tick_loop(self):
        import time
        while True:
            before = time.time()
            #TODO END GAME

            self.connection.push_events_to_client(self.board.tick(self.speed*self.refresh_rate,
                                                                  self.connection.get_last_events_client()[0]))
            now = time.time()
            time.sleep(before - now + self.refresh_rate if before - now + self.refresh_rate > 0 else 0)
            print("Waited", before - now + self.refresh_rate)

