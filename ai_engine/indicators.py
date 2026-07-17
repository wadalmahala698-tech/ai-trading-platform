def moving_average(prices, period=5):
    if len(prices) < period:
        return None

    recent_prices = prices[-period:]

    return sum(recent_prices) / period


print(moving_average([65000, 66000, 67000, 68000, 69000]))
