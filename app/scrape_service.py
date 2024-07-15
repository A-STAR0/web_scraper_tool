from typing import List

from app.scraper.schemas import ScrapeSettings, Product
from app.scraper.scraper_core import ScraperCore
from app.scraper.db_ops.storage import Storage
from app.scraper.notifier.notification_strategy import NotificationStrategy
import logging
logger = logging.getLogger(__name__)


class ScrapeService:
    def __init__(self, notifier: NotificationStrategy):
        self.notifier = notifier

    def scrape_products(self, settings: ScrapeSettings) -> List[Product]:
        try:
            scraper = ScraperCore(settings)
            products = scraper.scrape_data()
            storage = Storage()
            updated_products = 0
            for product in products:
                if storage.should_update(product):
                    storage.add_or_update_product(product)
                    updated_products += 1
            storage.save_data()
            message = f'Scraped {len(products)} products and updated {updated_products}in DB.'
            self.notifier.notify(message=message)
            return products
        except Exception as e:
            logger.error(f"Error while scraping products: {str(e)}")
            raise e
