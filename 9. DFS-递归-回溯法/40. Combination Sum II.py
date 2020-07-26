class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.helper(candidates, res, [], 0, target)
        return res

    def helper(self, nums, res, tmp, start, target):
        if sum(tmp) == target:
            res.append(list(tmp))
        else:
            for i in range(start, len(nums)):
                if sum(tmp) < target:
                    if i > 0 and nums[i-1] == nums[i] and i > start:
                        continue
                    tmp.append(nums[i])
                    self.helper(nums, res, tmp, i+1, target)
                    tmp.pop()
