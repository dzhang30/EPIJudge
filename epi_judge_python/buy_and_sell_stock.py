import sys

from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    absolute_max = -sys.maxsize
    min_index = 0
    if len(prices) > 1:
        for i in range(1, len(prices)):
            local_max = prices[i] - prices[min_index]
            if local_max < 0:
                min_index = i
            elif local_max  > absolute_max:
                absolute_max = local_max

    return absolute_max if absolute_max > 0 else 0

    # for price in prices[1:]:
    #     difference = price - lower_bound
    #     if difference >= 0 and difference > curr_max_profit:
    #         curr_max_profit = difference
    #     elif price < lower_bound:
    #         lower_bound = price
    #
    # if curr_max_profit < 0:
    #     return 0.0
    #
    # return curr_max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
