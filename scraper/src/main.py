import logging

from src.adapters.aldi import AldiAdapter
from src.adapters.base import ChainAdapter
from src.adapters.lidl import LidlAdapter
from src.adapters.penny import PennyAdapter
from src.adapters.spar import SparAdapter
from src.db import save_prices

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cheapjohn.scraper")

ADAPTERS: list[ChainAdapter] = [
    PennyAdapter(),
    AldiAdapter(),
    LidlAdapter(),
    SparAdapter(),
]


def run() -> None:
    for adapter in ADAPTERS:
        try:
            entries = adapter.fetch_prices()
        except NotImplementedError:
            logger.info("%s adapter meg nincs implementalva, kihagyva", adapter.chain)
            continue
        except Exception:
            logger.exception("%s adapter lekerdezese elbukott", adapter.chain)
            continue

        save_prices(entries)
        logger.info("%s: %d ar mentve", adapter.chain, len(entries))


if __name__ == "__main__":
    run()
