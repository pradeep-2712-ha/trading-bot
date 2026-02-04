def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError("side must be BUY or SELL")
    return side


def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError("order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("quantity must be greater than 0")
    return quantity


def validate_price(price):
    if price is None:
        raise ValueError("price is required for LIMIT orders")
    if price <= 0:
        raise ValueError("price must be greater than 0")
    return price
