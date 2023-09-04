from collections import deque
import sys
"""
리스트 병합
1. 리스트가 있을 때
2. 두 개의 리스트를 비교해서앞에서 부터 작은 원소들 순서대로 하나씩 새로운 리스트에 넣어줌.
"""
input_ls = []
for i in range(int(input())):
    input_ls.append(int(sys.stdin.readline().rstrip()))


def merge_list(list1, list2):
    merge_ls = []
    merge_ls = deque(merge_ls)
    while True:
        if not list1 and not list2:
            break
        elif not list1:
            merge_ls.extend(list2)
            break
        elif not list2:
            merge_ls.extend(list1)
            break
        elif list1[0] < list2[0]:
            merge_ls.append(list1[0])
            list1.popleft()
        elif list1[0] > list2[0]:
            merge_ls.append(list2[0])
            list2.popleft()
        elif list1[0] == list2[0]:
            merge_ls.append(list1[0])
            merge_ls.append(list2[0])
            list1.popleft()
            list2.popleft()
    return merge_ls

# 1. 2개씩 병합해서 최종적으로 n개의 리스트가 return 되게 하면 됨.
# 2. k번째에는 k/2개의 리스트의 개수가 존재하고 k-1번쨰에는 k-1/2개의 리스트가 존재
# 3. k-1 번째의 리스트가 병합되어서 return



def merge_sort(return_que):
    if len(return_que) == 1:
        return deque(return_que)

    return merge_list(merge_sort(return_que[:len(return_que) // 2]), merge_sort(return_que[len(return_que) // 2:]))


for i in merge_sort(input_ls):
    print(i)