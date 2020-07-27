class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict:
                    if dp[j]:
                        dp[i+1] = True
                        break
        return dp[-1]
