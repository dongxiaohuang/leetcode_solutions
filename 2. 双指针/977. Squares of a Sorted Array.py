class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        start_pos = 0
        while start_pos < len(A) and A[start_pos] < 0:
            start_pos += 1
        max_neg = start_pos - 1
        res = []
        while start_pos < len(A) and max_neg >= 0:
            if A[start_pos]**2 < A[max_neg]**2:
                res.append(A[start_pos]**2)
                start_pos += 1
            else:
                res.append(A[max_neg]**2)
                max_neg -= 1

        while start_pos < len(A):
            res.append(A[start_pos]**2)
            start_pos += 1

        while max_neg >= 0:
            res.append(A[max_neg]**2)
            max_neg -= 1

        return res
