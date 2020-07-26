class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(s, res, [], 0)
        return res

    def helper(self, s, res, tmp, start):
        if start == len(s):
            res.append(list(tmp))
        else:
            for i in range(start+1, len(s)+1):
                if self.isP(s[start:i]):
                    tmp.append(s[start:i])
                    self.helper(s, res, tmp, i)
                    tmp.pop()

    def isP(self, s):
        return s == s[::-1]
