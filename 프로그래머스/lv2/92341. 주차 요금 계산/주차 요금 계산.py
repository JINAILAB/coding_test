from collections import defaultdict
from math import ceil


def final_fee(in_time, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    if in_time <= base_time:
        return base_fee
    else:
        return base_fee + ceil((in_time - base_time) / unit_time) * unit_fee

def sum_time(time_list):
    sum_time_int = 0
    if len(time_list) % 2 == 1:
        time_list.append(1439)
        for i in range(len(time_list)//2):
            sum_time_int += (time_list[i*2+1] - time_list[i*2])
    else:
        for i in range(len(time_list)//2):
            sum_time_int += (time_list[i*2+1] - time_list[i*2])
    return sum_time_int



def solution(fees, records):
    list_dict = defaultdict(list)
    return_list = []
    for record in records:
        record_split = record.split()
        time_to_min = record_split[0].split(':')

        # 시간 분으로 바꿔주기
        time_to_min = int(time_to_min[0]) * 60 + int(time_to_min[1])
        list_dict[record_split[1]].append(time_to_min)

    index_list = sorted(list(list_dict.keys()))

    for i in index_list:
        return_list.append(final_fee(sum_time(list_dict[i]), fees))

    return return_list

