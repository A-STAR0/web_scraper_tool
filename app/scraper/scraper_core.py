import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from .schemas import ScrapeSettings, Product
import logging

logger = logging.getLogger(__name__)


class ScraperCore:
    def __init__(self, settings: ScrapeSettings, retry_attempts=3, retry_delay=3):
        self.base_url = os.getenv("TARGET_WEBSITE", "https://dentalstall.com/shop/page")

        self.settings = settings
        self.proxies = {
            "http": settings.proxy,
            "https": settings.proxy,
        } if settings.proxy else None
        self.retry_attempts = retry_attempts
        self.retry_delay = retry_delay

    def _scrape_page(self, page_num: int):
        url = f"{self.base_url}/{page_num}/"
        retries = self.retry_attempts
        while retries > 0:
            response = requests.get(url, proxies=self.proxies)
            if response.status_code == 200:
                return response.content
            retries -= 1
            logger.info(f'error while fetching page, waiting for : {self.retry_delay}')
            sleep(self.retry_delay)
        raise Exception(f"Error fetching page {page_num}")

    def scrape_data(self):
        logger.info("Starting the scraping process")
        products = []
        for page_num in range(1, self.settings.num_pages + 1):
            logger.info(f'scraping data for page: {page_num}')
            page_content = self._scrape_page(page_num)
            soup = BeautifulSoup(page_content, "html.parser")
            product_img = soup.findAll('div', {"class": "mf-product-thumbnail"})
            image_title_map_list = [{'image_url': img.find('img').get("data-lazy-src"),
                                     'title': img.find('img').get("title")}
                                    for img in product_img if img.find('img')]

            product_price = soup.findAll('div', {"class": "mf-product-price-box"})
            price_list = [str(price.find('span', class_='price').find('bdi').text.strip())
                          if price.find('span', class_='price') else '0'
                          for price in product_price if price.find('span')]
            logger.info(f'length of image_title_map_list = {len(image_title_map_list)} & '
                        f'price_list = {len(price_list)}')
            for img, price in zip(image_title_map_list, price_list):
                products.append(Product(product_title=img['title'], product_price=price, path_to_image=img['image_url']))
        return products
