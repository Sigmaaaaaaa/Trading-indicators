import MetaTrader5 as mt5
import pandas as pd
import time

symbol = "BTCUSD"
period = 20
timeframe = mt5.TIMEFRAME_M1

if not mt5.initialize():
    print("initialize() failed", mt5.last_error())
    quit()

try:
    while True:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
        data = pd.DataFrame(rates)

        # calculate SMA
        sma = data["close"].mean()

        # calculate EMA using pandas
        ema_series = data["close"].ewm(span=period, adjust=False).mean()
        ema = ema_series.iloc[-1]

        print(f"sma -> {sma:.2f} || ema -> {ema:.2f}")

        time.sleep(60)

except KeyboardInterrupt:
    print("Bot stopped manually")

finally:
    mt5.shutdown()