import json
import os

FILE = "data/prices.json"

def save_price(price):
    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append(price)

    with open(FILE, "w") as f:
        json.dump(data, f)


def get_prices():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)

    return []


save_price(65000)

print(get_prices())
