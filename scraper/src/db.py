import os

import psycopg

from src.models import PriceEntry


def get_connection() -> psycopg.Connection:
    dsn = os.environ["SCRAPER_DB_DSN"]
    return psycopg.connect(dsn)


def save_prices(entries: list[PriceEntry]) -> None:
    if not entries:
        return

    with get_connection() as conn, conn.cursor() as cur:
        cur.executemany(
            """
            INSERT INTO prices (chain, product_name, price, club_price, unit, scraped_at)
            VALUES (%(chain)s, %(product_name)s, %(price)s, %(club_price)s, %(unit)s, %(scraped_at)s)
            """,
            [entry.model_dump() for entry in entries],
        )
