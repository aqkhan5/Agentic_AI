# Personal Trading Skills & Cryptocurreny Journal 📈

A personal workspace housing cryptocurrency trading strategies, risk management setups, journals, and technical analysis data gathering guides.

---

## 📁 Project Structure

```
personal skills/
├── crypto-trading-strategy.md   # Crypto day trading strategy parameters & execution rules
├── real-time-data-guide.md      # Guide for gathering live indicators (TradingView, Binance, Python)
├── crypto_trading_journal.csv    # Logging spreadsheet for executed trades
└── README.md                    # Project overview (this file)
```

---

## 🛠️ Components

### 1. Crypto Day Trading Strategy (`crypto-trading-strategy.md`)
A formalized day trading system optimized for leverage and volatility on Binance Futures.

#### **Key System Parameters**
- **Pairs**: `BTC/USDT` and `ETH/USDT`
- **Timeframes**: `5-minute` & `15-minute`
- **Leverage**: `30x fixed` (cross margin)
- **Account Sizing**: Initial capital of `$200`
- **Risk Per Trade**: `$2 (1% of wallet)` requiring a margin of `$6.67` per trade
- **Risk-Reward Ratio**: `1:1` to `1:2` (Targeting `$2-4` reward)
- **Daily Caps**: Maximum of 3 wins OR 3 losses (immediate stop-trading rule)

#### **Signal Verification Checklist**
A signal is only valid if all criteria are satisfied:
1. Horizontal support/resistance rejection or swing high/low bounce.
2. RSI validation (Oversold `<30` for longs, Overbought `>70` for shorts, or clear divergence).
3. Confirming volume spike (higher than recent average volume).

For full execution details, see **[crypto-trading-strategy.md](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/AI%20driven%20development/personal%20skills/crypto-trading-strategy.md)**.

### 2. Real-Time Data Guide (`real-time-data-guide.md`)
A detailed guide demonstrating three methods to extract technical indicators (Price, Support/Resistance lines, 14-period RSI, Volume) needed to feed the trading strategy:
- **Method 1: TradingView (Recommended)**: Account setup, adding indicators, drawing key levels, and setting up real-time cross alerts.
- **Method 2: Binance Exchange Interface**: Direct futures platform chart configurations, drawing horizontal ranges, and using mobile app push notifications.
- **Method 3: Python Automation (CCXT)**: A boilerplate Python blueprint for programmatic REST/WebSocket API endpoints connecting to Binance to fetch real-time OHLCV candles, calculate RSI, and issue trade triggers.

For full setup guidelines, see **[real-time-data-guide.md](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/AI%20driven%20development/personal%20skills/real-time-data-guide.md)**.

### 3. Trading Journal (`crypto_trading_journal.csv`)
A spreadsheet structured to record and audit performance. It captures the date, asset pair, trade direction (Long/Short), leverage, entry/exit prices, fees, risk/reward metrics, and emotional notes to maintain self-discipline and track compound gains.
