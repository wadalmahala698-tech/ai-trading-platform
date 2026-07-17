class TradingAI:
    def __init__(self):
        self.name = "AI Trading Model"

    def predict(self, market_data):
        price = market_data["price"]

        if price < 55000:
            signal = "BUY"
            confidence = 0.75

        elif price > 65000:
            signal = "SELL"
            confidence = 0.75

        else:
            signal = "HOLD"
            confidence = 0.50

        return {
            "signal": signal,
            "confidence": confidence,
            "price_checked": price
        }


ai = TradingAI()
