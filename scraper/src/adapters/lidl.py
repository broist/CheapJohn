from src.adapters.base import ChainAdapter
from src.models import PriceEntry


class LidlAdapter(ChainAdapter):
    chain = "lidl"

    def fetch_prices(self) -> list[PriceEntry]:
        raise NotImplementedError
