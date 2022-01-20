from typing import List

def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    res = []
    intervals.sort()
    start, end = -1, -1
    for i, interval in enumerate(intervals):
        if i == 0:
            start, end = interval[0], interval[1]
            continue

        if interval[1] > end and interval[0] <= end:
            end = interval[1]
            if i == len(intervals) - 1:
                res.append([start, end])
        elif interval[0] > end:
            res.append([start, end])
            start, end = interval[0], interval[1]
            if i == len(intervals) - 1:
                res.append([start, end])
        elif interval[0] == start and interval[1] == end:
            if i == len(intervals) - 1:
                res.append([start, end])
            else:
                continue

    return res

# intervals = [[2,6], [1,3], [15,18], [8,10]]
# intervals = [[1,4], [4,5]]
#intervals = [[1,4], [1,4]]
intervals = [[1,4], [0,4]]
res = mergeIntervals(intervals)
print(res)