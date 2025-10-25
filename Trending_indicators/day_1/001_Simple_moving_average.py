import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time

symbol = "BTCUSD"
timeframe = mt5.TIMEFRAME_M1
period = 10

if not mt5.initialize():
    print("initialize() failed", mt5.last_error())
    quit()

try:
    while True:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
        data = pd.DataFrame(rates)

        # calculate sma of previos 10 candles

        sma = data["close"].mean()
        print(f"sma of last {period} : {sma:.5f}")

        time.sleep(60)

except KeyboardInterrupt:
    print("Bot stopped manually.")

finally:
    mt5.shutdown()
