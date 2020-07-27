class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(len(triangle)-2, -1, -1):
            tri = triangle[i]
            for j in range(len(tri)):
                tri[j] = tri[j]+min(triangle[i+1][j], triangle[i+1][j+1])
        # print(triangle)
        return triangle[0][0]
