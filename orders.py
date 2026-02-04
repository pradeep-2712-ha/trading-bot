print("orders.py loaded")

def place_market_order(client, symbol, side, quantity):
    return client.place_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

def place_limit_order(client, symbol, side, quantity, price):
    return client.place_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )
