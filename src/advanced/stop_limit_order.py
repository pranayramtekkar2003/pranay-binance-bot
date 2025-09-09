# It seems the stop_limit order is NOT for the Spot Test Network.
# Hence, no matter the number of parameter the transaction never goes through.
# It will work one we switch out from the Spot Test Network.


import argparse
from binance.exceptions import BinanceAPIException
from ..logger_setup import log
from ..client import binance_client

def stop_limit_order(symbol,side,quantity,price,stop_price):
    """
    Places a stop limit order on test network.
    """

    client = binance_client()
    symbol = symbol.upper()
    side = side.upper()

    if side not in ['BUY','SELL']:
        log.error(f"INVALID SIDE: {side} must be BUY or SELL.")
        return

    try:
        order = client.create_test_order(
            symbol = symbol,
            side = side,
            type = 'STOP_LOSS_LIMIT',
            timeInForce = 'GTC',
            quantity = quantity,
            price = price,
            stop_price = stop_price,
        )
        log.info("Stop-Limit Order placed successfully.")
    except BinanceAPIException as e:
        log.error(f"Error pplacing the stop-limit order. \n Error Message: {e}")
    except Exception as e:
        log.error(f"An unexpected error occured for the transaction.\n Error Message: {e}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser("Place a SpotNet stop-limit order.")
    parser.add_argument("symbol",type = str,help = "Trading Symbol ('eg: BTCUDST)")
    parser.add_argument("side",type = str,help = "BUY or SELL")
    parser.add_argument("quantity", type = float, help = "Order quantity")
    parser.add_argument("price",type = float, help = "The price at which limit order will be placed")
    parser.add_argument("stop_price",type = float, help = "The price that triggers the limit order.")

    args = parser.parse_args()
    stop_limit_order(args.symbol, args.side, args.quantity,args.price,args.stop_price)