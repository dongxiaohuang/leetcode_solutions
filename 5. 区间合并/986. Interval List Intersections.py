class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
                continue
            if A[i][0] > B[j][1]:
                j += 1
                continue
            # overlap
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            res.append([start, end])
            if A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
        return res
