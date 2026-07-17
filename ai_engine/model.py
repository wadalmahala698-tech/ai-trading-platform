import sys
sys.path.append(".")

import config

class TradingAI:
    def __init__(self):
        self.name = "AI Trading Model"

    def predict(self, market_data, history):
        price = market_data["price"]

        if len(history) == 0:
            return {
                "signal": "HOLD",
                "confidence": config.DEFAULT_CONFIDENCE
            }

        average = sum(history) / len(history)

        if price > average * config.BUY_THRESHOLD:
            signal = "BUY"
            confidence = 0.70

        elif price < average * config.SELL_THRESHOLD:
            signal = "SELL"
            confidence = 0.70

        else:
            signal = "HOLD"
            confidence = config.DEFAULT_CONFIDENCE

        return {
            "signal": signal,
            "confidence": confidence,
            "price": price,
            "average": round(average, 2)
        }


ai = TradingAI()
