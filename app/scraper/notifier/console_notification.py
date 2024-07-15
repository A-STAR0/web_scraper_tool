import logging
from .notification_strategy import NotificationStrategy

logger = logging.getLogger(__name__)


class ConsoleNotification(NotificationStrategy):
    def notify(self, message: str):
        logger.info(message)
