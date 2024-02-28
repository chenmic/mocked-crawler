from models.email import EmailNotification
from models.slack import SlackNotification

notification_channel_types = {
    "email": EmailNotification,
    "slack": SlackNotification,
}


class NotificationLogic:
    def notify(self, channel_types: list, channels: list):
        for channel_type in channel_types:
            notification_class = notification_channel_types.get(channel_type)
            if not notification_class:
                continue

            notification = notification_class(channels)
            notification.send()
