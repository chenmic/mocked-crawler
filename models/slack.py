from models.notification import Notification


class SlackNotification(Notification):
    SERVICE = "slack"
