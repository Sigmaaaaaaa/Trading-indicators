import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time

symbol = "BTCUSD"
timeframe = mt5.TIMEFRAME_M1
period = 20

if not mt5.initialize():
    print("initialize() failed! ", mt5.last_error())
    quit()

try:
    while True:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
        if rates is None or len(rates) < period:
            print("insufficient data received, Retrying...")
            time.sleep(60)
            continue

        data = pd.DataFrame(rates)
        close_prices = data["close"]

        # calculate sma
        sma = close_prices.mean()

        # calculate ema
        ema = close_prices.ewm(span=period, adjust=False).mean().iloc[-1]

        # calculate wma
        weights = np.arange(1, period + 1)
        wma = np.dot(close_prices, weights) / weights.sum()

        # Timestamp
        timestamp = pd.to_datetime(data["time"].iloc[-1], unit="s")

        # Signal logic
        if wma > sma and wma > ema:
            print(f"Time -> {timestamp} || 📈 Buy signal: WMA above EMA and SMA")
        elif wma < sma and wma < ema:
            print(f"Time -> {timestamp} || 📉 Sell signal: WMA below EMA and SMA")
        else:
            print(f"Time -> {timestamp} || ⏸️ Hold: No clear signal")

        time.sleep(1)

except KeyboardInterrupt:
    print("Bot stopped manually!")

finally:
    mt5.shutdown()