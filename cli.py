print("CLI FILE STARTED")
import argparse
import os
import logging
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

from bot.logging_config import setup_logging

def main():
    load_dotenv()
    setup_logging()

    parser = argparse.ArgumentParser("Binance Futures Testnet Trader")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise RuntimeError("Missing API credentials")

        client = BinanceFuturesClient(api_key, api_secret)

        print("\nOrder Request:", vars(args))

        if order_type == "MARKET":
            response = place_market_order(client, args.symbol, side, quantity)
        else:
            price = validate_price(args.price)
            response = place_limit_order(client, args.symbol, side, quantity, price)

        print("\nOrder Response:")
        print({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice"),
        })

        print("\n✅ Order placed successfully")

    except Exception as e:
        logging.exception("Order failed")
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
