import _thread


class Connection:

    def __init__(self):
        self.server_lock = _thread.allocate_lock()
        self.client_lock = _thread.allocate_lock()

        self.to_server = []
        self.to_clients = []

    def push_event_to_server(self, event):
        with self.server_lock:
            self.to_server.append(event)

    def push_event_to_client(self, event):
        with self.client_lock:
            self.to_clients.append(event)

    def push_events_to_server(self, events):
        with self.server_lock:
            self.to_server.extend(events)

    def push_events_to_client(self, events):
        with self.client_lock:
            self.to_clients.extend(events)

    def get_last_events_server(self):
        with self.server_lock:
            msgs = self.to_server.copy()
            self.to_server = []
            return msgs

    def get_last_events_client(self):
        with self.client_lock:
            msgs = self.to_clients.copy()
            self.to_clients = []
            return msgs

    def server_has_new_events(self):
        with self.server_lock:
            return len(self.to_server) > 0

    def client_has_new_events(self):
        with self.client_lock:
            return len(self.to_clients) > 0
