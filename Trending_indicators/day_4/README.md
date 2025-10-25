#  Real-Time BTCUSD Signal Bot using SMA, EMA, and WMA

This Python script connects to the MetaTrader 5 (MT5) and continuously monitors the BTCUSD market on a 1-minute timeframe. It calculates three key moving averages—Simple Moving Average (SMA), Exponential Moving Average (EMA), and Weighted Moving Average (WMA)—to generate real-time trading signals.

---

##  Features

- Connects to MetaTrader 5 using the `MetaTrader5` Python API
- Fetches real-time BTCUSD price data on a 1-minute interval
- Calculates:
  - **SMA** – Simple Moving Average
  - **EMA** – Exponential Moving Average
  - **WMA** – Weighted Moving Average
- Generates trading signals:
  -  **Buy** when WMA > EMA and SMA
  -  **Sell** when WMA < EMA and SMA
  -  **Hold** otherwise
- Gracefully handles data unavailability and supports manual interruption

---

##  Requirements

- Python 3.8+
- MetaTrader 5 terminal (installed and logged in)
- Python packages:
  ```bash
  pip install MetaTrader5 pandas numpy
