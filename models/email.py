from models.notification import Notification


class EmailNotification(Notification):
    SERVICE = "email"
