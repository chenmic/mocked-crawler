class Notification:
    def __init__(self, recipients: list):
        self.recipients = recipients

    def send(self):
        for recipient in self.recipients:
            print(f"Notifying {recipient} via {self.SERVICE}")
