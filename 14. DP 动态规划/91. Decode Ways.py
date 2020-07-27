class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]*len(s)
        for i, char in enumerate(s):
            if int(char) > 0 and int(char) <= 9:
                if i > 0 and int(s[i-1:i+1]) >= 11 and int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-1]+dp[i-2]
                else:
                    dp[i] = dp[i-1]
            elif int(char) == 0:
                if i >= 1 and (int(s[i-1:i+1]) == 10 or int(s[i-1:i+1]) == 20):
                    if i == 1:
                        dp[i] = 1
                    else:
                        dp[i] = dp[i-2]
                else:
                    return '0'
            else:
                return '0'
        return dp[-1]
