class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',

        }
        if not digits:
            return []
        self.helper(res, digits, d_map, '', 0)
        return res

    def helper(self, res, digits, d_map, tmp, idx):
        if idx == len(digits):
            res.append(tmp)
        else:
            for char in d_map[digits[idx]]:
                tmp += char
                self.helper(res, digits, d_map, tmp, idx+1)
                tmp = tmp[:-1]
