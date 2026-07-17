class TradingAI:
    def __init__(self):
        self.name = "AI Trading Model"

    def predict(self, market_data, history):
        price = market_data["price"]

        if len(history) == 0:
            return {
                "signal": "HOLD",
                "confidence": 0.50
            }

        average = sum(history) / len(history)

        if price > average:
            signal = "BUY"
            confidence = 0.70

        elif price < average:
            signal = "SELL"
            confidence = 0.70

        else:
            signal = "HOLD"
            confidence = 0.50

        return {
            "signal": signal,
            "confidence": confidence,
            "price": price,
            "average": round(average, 2)
        }


ai = TradingAI()
