from src.utils import calculate_total


def run_application():
    print("AI Software Engineering Agent - Sample Application")

    prices = [100, 200, 300]
    total = calculate_total(prices)

    print("Product prices:", prices)
    print("Total:", total)
