import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Parameters
symbol = "BTCUSD"
timeframe = mt5.TIMEFRAME_M5
period_1 = 12  # Fast EMA
period_2 = 26  # Slow EMA
period_3 = 9   # Signal line

# Initialize MT5 connection
if not mt5.initialize():
    logging.error("MT5 initialization failed")
    quit()

try:
    while True:
        # Fetch price data
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, max(period_1, period_2) + 50)
        if rates is None or len(rates) < max(period_1, period_2):
            logging.warning("Failed to retrieve sufficient rates")
            time.sleep(5)
            continue

        # Convert to DataFrame
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')

        # Calculate MACD components
        df['EMA_fast'] = df['close'].ewm(span=period_1, adjust=False).mean()
        df['EMA_slow'] = df['close'].ewm(span=period_2, adjust=False).mean()
        df['MACD'] = df['EMA_fast'] - df['EMA_slow']
        df['Signal'] = df['MACD'].ewm(span=period_3, adjust=False).mean()
        df['Histogram'] = df['MACD'] - df['Signal']

        # Print latest MACD values
        latest = df[['time', 'close', 'MACD', 'Signal', 'Histogram']].tail(1)
        logging.info(f"\n{latest}")

        # Detect Buy/Sell Signals
        if df['MACD'].iloc[-2] < df['Signal'].iloc[-2] and df['MACD'].iloc[-1] > df['Signal'].iloc[-1]:
            logging.info("📈 Buy Signal Detected")
        elif df['MACD'].iloc[-2] > df['Signal'].iloc[-2] and df['MACD'].iloc[-1] < df['Signal'].iloc[-1]:
            logging.info("📉 Sell Signal Detected")

        time.sleep(5)  # Wait for next 5-minute candle

except KeyboardInterrupt:
    logging.info("Stopped by user")

finally:
    logging.info("Shutting down MT5 connection")
    mt5.shutdown()