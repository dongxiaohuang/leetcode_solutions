class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        if intervals[0][0] > newInterval[1]:
            return [newInterval]+intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals+[newInterval]

        i = 0
        res = []
        has_insert = False
        while i < len(intervals):
            interval = intervals[i]
            if not has_insert:
                if interval[0] <= newInterval[0]:
                    res.append(interval)
                    i += 1
                else:
                    if not res or res[-1][1] < newInterval[0]:
                        res.append(newInterval)
                    else:
                        res[-1][1] = max(res[-1][1], newInterval[1])
                    has_insert = True
            else:
                if res[-1][1] < interval[0]:
                    res.append(interval)
                else:
                    res[-1][1] = max(res[-1][1], interval[1])
                i += 1
        if not has_insert:
            res[-1][1] = max(res[-1][1], newInterval[1])
        return res
