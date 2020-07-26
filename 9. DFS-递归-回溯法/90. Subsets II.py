class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.helper(nums, res, [], 0)
        return res

    def helper(self, nums, res, tmp, start):
        res.append(list(tmp))

        for i in range(start, len(nums)):
            if i > start and i > 0 and nums[i] == nums[i-1]:
                continue

            tmp.append(nums[i])
            self.helper(nums, res, tmp, i+1)
            tmp.pop()
