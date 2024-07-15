import sys
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from app.scraper.notifier.console_notification import ConsoleNotification
from app.scraper.schemas import ScrapeSettings, Product
from app.scrape_service import ScrapeService
from app.auth import get_api_key
import logging

app = FastAPI()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


@app.get("/")
def health():
    return {"message": "Welcome to the Web Scraper Service."}


@app.post("/scrape", response_model=List[Product])
def scrape_products(settings: ScrapeSettings, api_key: str = Depends(get_api_key)):
    try:
        logger.info(f'scraping data for settings: {settings}')
        # Create an instance of the notification strategy
        console_notifier = ConsoleNotification()
        products = ScrapeService(notifier=console_notifier).scrape_products(settings)
        logger.info("Scraping completed successfully")
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while scraping data: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
