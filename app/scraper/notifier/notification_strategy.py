from abc import ABC, abstractmethod
import logging
logger = logging.getLogger(__name__)


class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass



#
# class Notifier:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def notify_scraping_summary(num_scraped, num_updated):
#         logger.info(f"Scraped {num_scraped} products and updated {num_updated}in DB.")
