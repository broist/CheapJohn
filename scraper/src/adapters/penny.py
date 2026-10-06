from src.adapters.base import ChainAdapter
from src.models import PriceEntry


class PennyAdapter(ChainAdapter):
    chain = "penny"

    def fetch_prices(self) -> list[PriceEntry]:
        raise NotImplementedError
