class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(s)+1) for i in range(len(p)+1)]
        for i in range(len(p)+1):
            for j in range(len(s)+1):
                if i == 0:
                    if j == 0:
                        dp[i][j] = True
                    continue
                if j == 0:
                    if i >= 2 and p[i-1] == "*":
                        dp[i][j] = dp[i-2][j]
                    continue
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                if p[i-1] == '*':
                    dp[i][j] = dp[i-2][j]
                    if s[j-1] == p[i-2] or p[i-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[-1][-1]
