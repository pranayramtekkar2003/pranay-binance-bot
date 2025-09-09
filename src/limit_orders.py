import argparse
from binance.exceptions import BinanceAPIException
from .client import binance_client
from .logger_setup import log

def place_limit_order(symbol, side, quantity, price):
    """
    Places limit orders for Test network
    """

    client = binance_client()
    side = side.upper()
    symbol = symbol.upper()

    if side not in ['BUY','SELL']:
        log.error(f"INVALID SIDE: {side} must be BUY or SELL.")
        return
    if price <= 0:
        log.error("Price should be greater than 0.")
        return
    
    try:
        log.info(f"Placing a limit order: {side} {quantity} {symbol} at {price}")

        order = client.create_test_order(
            symbol = symbol,
            side = side,
            type = 'LIMIT',
            timeInForce = 'GTC',
            quantity = quantity,
            price = price,
        )
        log.info(f"Successfully created a limit order.")
    except BinanceAPIException as e:
        log.error(f"Error placing limit orderfor {symbol}. \n Error Message:{e}")
    except Exception as e:
        log.error(f"An unexpected error occured for transaction. \n Error Message: {e}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Place a Binance Futures limit order.')
    parser.add_argument('symbol', type=str, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side (BUY or SELL)')
    parser.add_argument('quantity', type=float, help='Order quantity')
    parser.add_argument('price', type=float, help='Order price')

    args = parser.parse_args()
    place_limit_order(args.symbol, args.side, args.quantity, args.price)