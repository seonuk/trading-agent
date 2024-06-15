import pandas as pd
import pandas_ta as ta
from binance import Client

from config.binance_client import client


def get_historical_klines(symbol, interval, start_str):
    klines = client.get_historical_klines(symbol, interval, start_str)
    data = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    data['close'] = data['close'].astype(float)
    return data

def calculate_rsi(data, period=14):
    data['rsi'] = ta.rsi(data['close'], length=14)
    return data

def get_rsi():

    symbol = 'BTCUSDT'
    interval = Client.KLINE_INTERVAL_1HOUR
    start_str = '1 month ago UTC'
    data = get_historical_klines(symbol, interval, start_str)

    # RSI 계산
    data['rsi'] = ta.rsi(data['close'], length=14)

    return data[['timestamp', 'close', 'rsi']].tail()