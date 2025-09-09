# This also not supports the oco_order functionality for the test network.
# The spot Test network has its limitations and would not be able to carry all the relevant adavance function it seems.
#Hence, I have only coded the structure for this and few minor tweaks would make it sufficient for the real Binance network.

import argparse
from binance.exceptions import BinanceAPIException
from ..client import binance_client
from ..logger_setup import log

def oco_order(symbol,side,quantity,price,stop_price,stop_limit_price):
    """
    Places one-canels-other order on spot network.
    """

    client = binance_client()
    side = side.upper()
    symbol = symbol.upper()

    #Stem for the opposite order
    oppo_side = 'BUY' if side == 'SELL' else 'SELL' 

    try:
        log.info(f"Placing OCO order for {symbol}")
        log.info(f"     Profit at {oppo_side} at {price}")
        log.info(f"     Loss at {oppo_side} triggered at {stop_price}")

        order = client.create_oco_order(
            symbol = symbol,
            side = side,
            quantity = quantity,
            price = price,
            stopPrice = stop_price,
            stopLimitPrice = stop_limit_price,
            stopLimitTimeInForce = 'GTC',
            aboveType = "EXPIRE_MAKER",
            belowType = "EXPIRE_MAKER"
        )

        log.info(f"Successfully placed OCO order at Test network.")

    except BinanceAPIException as e:
        log.error(f"Error placing OCO order for Test Network.\n Error Message: {e}")
    except Exception as e:
        log.error(f"An unexpected error occured during Transaction.\nError Message: {e}")

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser("Place a SpotNet OCO order.")
    parser.add_argument("symbol",type = str,help = "Trading Symbol ('eg: BTCUDST)")
    parser.add_argument("side",type = str,help = "BUY or SELL")
    parser.add_argument("quantity", type = float, help = "Order quantity")
    parser.add_argument("price",type = float, help = "The price at which limit order will be placed")
    parser.add_argument("stopPrice",type = float, help = "The price that triggers the limit order.")
    parser.add_argument("stopLimitPrice", type = float, help= "Actual limit price at which order is placed in order book")

    args = parser.parse_args()
    oco_order(args.symbol, args.side, args.quantity, args.price, args.stopPrice, args.stopLimitPrice)
