import argparse
from binance.exceptions import BinanceAPIException
from .client import binance_client
from .logger_setup import log

def market_order(symbol, side, quantity):
    """
    Placing market orders on binance SpotTestNet
    """
    client = binance_client()
    side = side.upper()
    symbol = symbol.upper()

    if side not in ['BUY','SELL']:
        log.error(f"INVALID SIDE: {side} must be BUY or SELL.")

    try:
        log.info(f"Placing Test market order: {side} {quantity} {symbol}")
        order = client.create_test_order(
            symbol = symbol,
            side = side,
            type = 'MARKET',
            quantity = quantity,
        )
        log.info(f"Test Market Order Placed successfully.")

    except BinanceAPIException as e:
        log.error(f"Error placing market order for {symbol} : {e}")
    except Exception as e:
        log.error(f"An unexpected error occured for the transaction. \n Error Mesage: {e}")

    
if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(description="Place a Binance Futures market order")
    parser.add_argument('symbol',type=str, help='Trading symbol [Eg: BTCUSDT]')
    parser.add_argument('side',type=str,choices=["BUY","SELL"],help="Order Side (BUY or SELL)")
    parser.add_argument('quantity', type=float, help="Order quantity")

    args = parser.parse_args()
    market_order(args.symbol, args.side, args.quantity)