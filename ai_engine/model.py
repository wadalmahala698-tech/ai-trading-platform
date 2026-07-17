import sys
sys.path.append(".")

import config
from indicators import moving_average


class TradingAI:
    def __init__(self):
        self.name = "AI Trading Model"

    def predict(self, market_data, history):
        price = market_data["price"]

        ma = moving_average(history)

        if ma is None:
            return {
                "signal": "HOLD",
                "confidence": config.DEFAULT_CONFIDENCE
            }

        if price > ma:
            signal = "BUY"
            confidence = 0.70

        elif price < ma:
            signal = "SELL"
            confidence = 0.70

        else:
            signal = "HOLD"
            confidence = config.DEFAULT_CONFIDENCE

        return {
            "signal": signal,
            "confidence": confidence,
            "price": price,
            "moving_average": round(ma, 2)
        }


ai = TradingAI()
