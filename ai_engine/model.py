class TradingAI:
    def __init__(self):
        self.name = "AI Trading Model"

    def predict(self, market_data):
        return {
            "signal": "HOLD",
            "confidence": 0.50
        }

ai = TradingAI()

print(ai.predict({}))
