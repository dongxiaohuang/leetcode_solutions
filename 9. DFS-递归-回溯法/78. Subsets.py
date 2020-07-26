class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], 0, res)
        return res

    def helper(self, nums, tmp, start, res):
        res.append(list(tmp))
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.helper(nums, tmp, i+1, res)
            tmp.pop()
