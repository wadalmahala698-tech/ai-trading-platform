class RiskManager:
    def __init__(self, balance=1000, risk_percent=1):
        self.balance = balance
        self.risk_percent = risk_percent

    def position_size(self, price):
        risk_amount = self.balance * (self.risk_percent / 100)

        size = risk_amount / price

        return round(size, 6)

    def check_trade(self, signal):
        if signal in ["BUY", "SELL"]:
            return "TRADE_ALLOWED"

        return "NO_TRADE"


risk = RiskManager()

print(risk.position_size(68000))
print(risk.check_trade("BUY"))
