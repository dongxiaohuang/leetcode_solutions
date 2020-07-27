class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) <= 1:
            return s
        dp = [[False]*len(s) for i in range(len(s))]
        res = s[0]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if dp[i+1][j-1] or j-i == 1:
                        dp[i][j] = True
                        if j-i + 1 > len(res):
                            res = s[i:j+1]
        # print(dp)
        return res
