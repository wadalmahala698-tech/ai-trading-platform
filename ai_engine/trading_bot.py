import sys
sys.path.append("data")

from market_data import MarketData
from model import TradingAI
from price_history import get_prices, save_price
from risk_manager import RiskManager

market = MarketData()
ai = TradingAI()
risk = RiskManager()

data = market.get_price("BTCUSDT")

save_price(data["price"])

history = get_prices()

decision = ai.predict(data, history)

trade_status = risk.check_trade(decision["signal"])
size = risk.position_size(data["price"])

print("Market Data:")
print(data)

print("AI Decision:")
print(decision)

print("Risk Status:")
print(trade_status)

print("Position Size:")
print(size)
