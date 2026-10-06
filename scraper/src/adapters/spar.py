from src.adapters.base import ChainAdapter
from src.models import PriceEntry


class SparAdapter(ChainAdapter):
    chain = "spar"

    def fetch_prices(self) -> list[PriceEntry]:
        raise NotImplementedError
