import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time

symbol = "BTCUSD"
timeframe = mt5.TIMEFRAME_M1
period = 20
sleep_interval = 60 

# Initialize MetaTrader 5
if not mt5.initialize():
    print("initialize() failed:", mt5.last_error())
    quit()

try:
    while True:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
        if rates is None or len(rates) < period:
            print("insufficient data received, Retrying...")
            time.sleep(sleep_interval)
            continue

        data = pd.DataFrame(rates)
        close_price = data["close"]

        # calculate wma
        weights = np.arange(1, period + 1)
        wma = np.dot(close_price, weights) / weights.sum()

        # timestamp
        timestamp = pd.to_datetime(data["time"].iloc[-1], unit="s")

        # output
        print(f"{timestamp} -> WMA: {wma:.2f}")
        
        time.sleep(sleep_interval)

except KeyboardInterrupt:
    print("Bot stopped manually!")

finally:
    mt5.shutdown()