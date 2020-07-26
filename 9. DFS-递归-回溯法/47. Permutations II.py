class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False]*len(nums)
        self.helper(nums, res, [], used)
        return res

    def helper(self, nums, res, tmp, used):
        if len(tmp) == len(nums):
            res.append(list(tmp))
        else:
            for i in range(len(used)):
                if not used[i]:
                    if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                        continue
                    tmp.append(nums[i])
                    used[i] = True
                    self.helper(nums, res, tmp, used)
                    used[i] = False
                    tmp.pop()
