from typing import Tuple, List
from enum import Enum


# Modify Me
data = {
    "weight": 225,
    "sex": "m",
    "time": 0.25,
    "ingredients": [
        [1, 0.24],
        [1, 0.4],
        [1, 0.16]
    ]
}


class R(Enum):
    """Sex constant R"""
    m = 0.68
    f = 0.55


def calc_bac(alcohol: float, weight: float, t: float, sex: R) -> float:
    """Takes quantity of alcohol, weight, time since consumed, and enum R."""
    bac = alcohol / (weight * sex.value)
    return bac - (t * 0.015)


def calc_abv(ingredients: List[Tuple[float, float]]) -> float:
    """Takes a list of ingredients (qty,abv) and returns the total abv for the
    drink.
    """
    total_vol = 0
    numerator = 0
    for qty, abv in ingredients:
        total_vol += qty
        numerator += qty * abv
    return numerator / total_vol


def calc_alcohol(ingredients: List[Tuple[float, float]]) -> float:
    abv = calc_abv(ingredients)
    qty = sum([qty for qty, _ in ingredients])
    return qty * abv


if __name__ == "__main__":
    abv = calc_abv(data["ingredients"])
    print(f"Your drink had an abv of {abv}")
    alcohol = calc_alcohol(data["ingredients"])
    print(f"You consumed {alcohol} alcohol")
    bac = calc_bac(alcohol, data["weight"], data["time"], getattr(R, data["sex"]))
    print(f"You have a bac of {bac}")
