def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total


def calculate_average(prices):
    if not prices:
        return 0

    return sum(prices) / len(prices)
