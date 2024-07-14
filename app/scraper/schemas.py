from pydantic import BaseModel
from typing import Optional


class ScrapeSettings(BaseModel):
    num_pages: Optional[int] = 5
    proxy: Optional[str] = None


class Product(BaseModel):
    product_title: str
    product_price: str
    path_to_image: str
