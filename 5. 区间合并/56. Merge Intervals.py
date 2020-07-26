class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        starts.sort()
        ends.sort()
        res = []
        for start, end in zip(starts, ends):
            if not res:
                res.append([start, end])
            else:
                prev_itv = res[-1]
                if start > prev_itv[1]:
                    res.append([start, end])
                else:
                    if end <= prev_itv[1]:
                        continue
                    else:
                        prev_itv[1] = end
        return res
