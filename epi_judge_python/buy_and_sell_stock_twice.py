from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    profit_1 = 0
    profit_2 = 0

    start_next = False
    min_price = float('inf')
    for i in range(len(prices)):
        curr_val = prices[i]
        if curr_val < min_price:
            min_price = curr_val
            start_next = True if profit_1 > 0 else False
        else:
            local_diff = curr_val - min_price
            if start_next:
                temp = profit_2
                if profit_2 <= local_diff:
                    profit_2 = local_diff
                    if profit_1 < temp:
                        profit_1 = temp
                elif profit_1 <= local_diff:
                    profit_1 = profit_2
                    profit_2 = local_diff
                start_next = False
            else:
                if not profit_1 or (profit_1 and not profit_2):
                    profit_1 = max(profit_1, local_diff)
                else:
                    profit_2 = max(profit_2, local_diff)

    return profit_1 + profit_2


def get_free_time(cal_a, cal_b, meeting_duration):
    merged_cals = cal_a + cal_b
    merged_cals.sort(key=lambda x: (x[0], x[1]))

    result = []
    prev_end = merged_cals[0][1]
    for i in range(1, len(merged_cals)):
        cur_begin = merged_cals[i][0]
        cur_end = merged_cals[i][1]
        # if cur_begin <= prev_end:
        #     prev_end = cur_end
        # else:
        #     if cur_begin - prev_end >= meeting_duration:
        #         result.append((prev_end, cur_begin))
        #     prev_end = cur_end
        if cur_begin > prev_end and cur_begin - prev_end >= meeting_duration:
            result.append((prev_end, cur_begin))

        prev_end = cur_end

    return result


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main("buy_and_sell_stock_twice.py",
    #                                    "buy_and_sell_stock_twice.tsv",
    #                                    buy_and_sell_stock_twice))
    # arr = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    # print(buy_and_sell_stock_twice(arr))

    from pprint import pprint

    x = [[900, 1030], [1200, 1300], [1600, 1800]]
    y = [[1000, 1130], [1230, 1430], [1430, 1500], [1600, 1700]]

    pprint(get_free_time(x, y, 30))
