class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or not s:
            return 0
        res = 1
        start = 0
        ch_map = {}
        for i in range(len(s)):
            offer = s[i]
            if offer not in ch_map:
                ch_map[offer] = i
            else:
                if ch_map[offer] < start:  # not in the current seq
                    ch_map[offer] = i
                else:
                    start = ch_map[offer]+1
                    ch_map[offer] = i
            res = max(i-start+1, res)
        return res
