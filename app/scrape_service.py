from typing import List

from app.scraper.schemas import ScrapeSettings, Product
from app.scraper.scraper_core import ScraperCore
from app.scraper.db_ops.storage import Storage
from app.scraper.notifier.notification import Notifier


class ScrapeService:

    @staticmethod
    def scrape_products(settings: ScrapeSettings) -> List[Product]:
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
            Notifier().notify_scraping_summary(num_scraped=len(products), num_updated=updated_products)
            return products
        except Exception as e:
            print(f"Error while scraping products: {str(e)}")
            raise e
