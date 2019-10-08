import sys

from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    curr_max_profit = -sys.maxsize
    lower_bound = prices[0]

    for price in prices[1:]:
        difference = price - lower_bound
        if difference >= 0 and difference > curr_max_profit:
            curr_max_profit = difference
        elif price < lower_bound:
            lower_bound = price

    if curr_max_profit < 0:
        return 0.0

    return curr_max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
