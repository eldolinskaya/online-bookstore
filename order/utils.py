def get_price(price):
    if price >=100:
        return price, 0
    else:
        return (price + 10), 10