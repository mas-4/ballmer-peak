from datetime import datetime as dt
from typing import Tuple, List
from enum import Enum

DATE = dt.now()

# Modify Me
data = {
    "weight": 225,      # in pounts
    "sex": "m",         # m or f
    "cocktails": [
        {
            "name": "Negroni",
            "time": DATE.replace(hour=17, minute=30),   # 24 hour time
            "ingredients": [
                (1, 0.24),  # units (ounces, abv as decimal)
                (1, 0.4),
                (1, 0.16)
            ]
        },
        {
            "name": "Negroni",
            "time": DATE.replace(hour=17, minute=45),
            "ingredients": [
                (1, 0.24),
                (1, 0.4),
                (1, 0.16)
            ]
        }
    ]
}


class R(Enum):
    """Sex constant R"""
    m = 0.68
    f = 0.55


def calc_bac(alcohol: float, weight: float, t: float, sex: R) -> float:
    """Takes quantity of alcohol in ounces, weight in pounds, time since
    consumed in hours, and enum R.
    """
    bac = alcohol / (weight * 16 * sex.value)
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
    return (numerator / total_vol) * 100


def calc_alcohol(ingredients: List[Tuple[float, float]]) -> float:
    abv = calc_abv(ingredients)
    qty = sum([qty for qty, _ in ingredients])
    return qty * abv


if __name__ == "__main__":
    total_bac = 0
    for drink in data['cocktails']:
        abv = calc_abv(drink['ingredients'])
        print(f"Your {drink['name']} had an abv of {abv}")
        alcohol = calc_alcohol(drink["ingredients"])
        print(f"That equates to {alcohol} ounces of alcohol.")
        hours = (DATE-drink["time"]).seconds / 60 / 60
        bac = calc_bac(alcohol, data["weight"], hours, getattr(R, data["sex"]))
        print(bac)
        total_bac += min(bac, 0)
    print(f"You have a bac of {total_bac}")
