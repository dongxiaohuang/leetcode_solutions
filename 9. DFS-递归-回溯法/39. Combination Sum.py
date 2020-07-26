class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates, res, [], 0, target)
        return res

    def helper(self, nums, res,  tmp, start, target):
        if sum(tmp) == target:
            res.append(list(tmp))
        else:
            for i in range(start, len(nums)):
                if sum(tmp) < target:
                    tmp.append(nums[i])
                    self.helper(nums, res, tmp, i+1, target)
                    tmp.pop()
