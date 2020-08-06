# take 2 people's calendar and return intervals where they can have a meeting


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
