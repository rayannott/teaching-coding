"""This module contains the currency conversion functions
that imitate the real-world currency conversion rates."""

import pathlib
import json


RATES_FILE = pathlib.Path("utils") / "rates.json"

# mapping of currency codes to "how much 1 unit of the currency is worth in USD"
RATES = json.loads(RATES_FILE.read_text())


def to_usd(amount: float, currency: str) -> float:
    """Convert the given amount from the given currency to USD."""
    assert currency in RATES, f"Unknown currency: {currency}"
    return amount * RATES[currency]


def from_usd(amount: float, currency: str) -> float:
    """Convert the given amount from USD to the given currency."""
    assert currency in RATES, f"Unknown currency: {currency}"
    return amount / RATES[currency]


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """Convert the given amount from the given currency to the other currency.
    Round the result to 2 decimal places.
    """
    raise NotImplementedError("TODO: implement the conversion logic here")
