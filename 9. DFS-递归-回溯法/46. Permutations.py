class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False]*len(nums)
        self.helper(nums, res, [], used)
        return res

    def helper(self, nums, res, tmp, used):
        if len(tmp) == len(nums):
            res.append(list(tmp))
        else:
            for i in range(len(used)):
                if not used[i]:
                    used[i] = True
                    tmp.append(nums[i])
                    self.helper(nums, res, tmp, used)
                    used[i] = False
                    tmp.pop()
