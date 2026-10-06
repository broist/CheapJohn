from datetime import date

from pydantic import BaseModel


class PriceEntry(BaseModel):
    chain: str
    product_name: str
    price: float
    club_price: float | None = None
    unit: str
    scraped_at: date
