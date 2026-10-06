from src.adapters.base import ChainAdapter
from src.models import PriceEntry


class AldiAdapter(ChainAdapter):
    chain = "aldi"

    def fetch_prices(self) -> list[PriceEntry]:
        raise NotImplementedError
