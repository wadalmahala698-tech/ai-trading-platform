from market_data import MarketData
from model import TradingAI

market = MarketData()
ai = TradingAI()

data = market.get_price("BTCUSDT")

decision = ai.predict(data)

print("Market Data:")
print(data)

print("AI Decision:")
print(decision)
