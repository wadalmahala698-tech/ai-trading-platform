import random
import time

class MarketData:
    def get_price(self, symbol):
        price = round(random.uniform(50000, 70000), 2)

        return {
            "symbol": symbol,
            "price": price,
            "time": time.time()
        }


market = MarketData()

print(market.get_price("BTCUSDT"))
