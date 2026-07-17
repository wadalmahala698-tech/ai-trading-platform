import sys
sys.path.append("data")

from market_data import MarketData
from model import TradingAI
from price_history import get_prices, save_price

market = MarketData()
ai = TradingAI()

data = market.get_price("BTCUSDT")

save_price(data["price"])

history = get_prices()

decision = ai.predict(data, history)

print("Market Data:")
print(data)

print("Price History:")
print(history)

print("AI Decision:")
print(decision)
