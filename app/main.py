from fastapi import FastAPI, Depends, HTTPException
from typing import List
from scraper.schemas import ScrapeSettings, Product
from scrape_service import ScrapeService
from auth import get_api_key

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Web Scraper API"}


@app.post("/scrape", response_model=List[Product])
def scrape_products(settings: ScrapeSettings, api_key: str = Depends(get_api_key)):
    try:
        products = ScrapeService().scrape_products(settings)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while scraping data: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
