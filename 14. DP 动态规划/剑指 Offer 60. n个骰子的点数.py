class Solution:
    def twoSum(self, n: int) -> List[float]:

        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1

        for i in range(2,n+1):
            for j in range(i,i*6+1):
                for k in range(1,7):
                    if j >= k+1:
                        dp[i][j] +=dp[i-1][j-k]
        res = []
        for i in range(n,n*6+1):
            res.append(dp[n][i]*1.0/6**n)
        return res

作者：up2m
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/rong-yi-li-jie-de-pythondong-tai-gui-hua-fang-fa-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。