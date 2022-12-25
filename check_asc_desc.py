"""
Write a Python function that checks that a given list is sorted in
ascending order, descant order or not sorted. It should return 1 for
ascending and -1 for descending and 0 for not sorted.
example:
[9, 8, 7, 6, 5, 4, 3, 2, 1] //return -1
[1, 2, 3, 4, 5, 6, 7, 8, 9] //return 1
[3, 5, 2, 9, 3] //return 0

"""


def check_asc_desc(listSample):
    length = len(listSample) - 1
    if listSample[0] > listSample[1]:
        res = -1
    else:
        res = 1
    #     range not inclusive range(1,6) - 1, 2, 3, 4, 5
    for i in range(1, length):
        curr_val = listSample[i]
        next_val = listSample[i + 1]
        if res == -1:
            if curr_val > next_val:
                continue
            else:
                return 0

        else:
            if curr_val < next_val:
                continue
            else:
                return 0

    return res


list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = [3, 5, 2, 9, 3]
print(check_asc_desc(list1) == -1)
print(check_asc_desc(list2) == 1)
print(check_asc_desc(list3) == 0)
