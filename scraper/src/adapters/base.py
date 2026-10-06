from abc import ABC, abstractmethod

from src.models import PriceEntry


class ChainAdapter(ABC):
    """Egy diszkontlánc árlekérdezését végző adapter."""

    chain: str

    @abstractmethod
    def fetch_prices(self) -> list[PriceEntry]:
        """Lekéri az aktuális árakat a láncnál. Egy hívás = egy teljes katalógus-snapshot."""
        raise NotImplementedError
