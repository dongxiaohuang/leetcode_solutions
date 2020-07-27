class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = list(s)
        self.revert(s, 0, len(s)-1)
        start = 0
        end = 0
        while start < len(s):
            if s[start] == ' ':
                start += 1
                end += 1
            elif end == len(s) or s[end] == ' ':
                self.revert(s, start, end-1)
                start = end
            else:
                end += 1

        return ''.join(s)

    def revert(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
