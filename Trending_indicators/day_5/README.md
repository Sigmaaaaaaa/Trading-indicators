#  BTCUSD MACD Signal Bot (MetaTrader 5)

This Python script connects to MetaTrader 5 and monitors BTCUSD on a 5-minute timeframe. It calculates the MACD indicator and generates real-time buy/sell signals based on crossover logic.

---

##  Features

- Connects to MetaTrader 5 using the `MetaTrader5` Python API
- Calculates:
  - Fast EMA (12-period)
  - Slow EMA (26-period)
  - MACD line (EMA_fast - EMA_slow)
  - Signal line (9-period EMA of MACD)
  - Histogram (MACD - Signal)
- Detects crossover signals:
  -  Buy when MACD crosses above Signal
  -  Sell when MACD crosses below Signal
- Logs output with timestamps using Python’s `logging` module
- Runs continuously with graceful shutdown on `Ctrl + C`

---

##  Requirements

- MetaTrader 5 terminal (installed and logged in)
- Python 3.8+
- Required packages:
  ```bash
  pip install MetaTrader5 pandas numpy

