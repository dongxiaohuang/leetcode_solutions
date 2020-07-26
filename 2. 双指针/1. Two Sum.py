class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}
        for i in range(len(nums)):
            if (target-nums[i]) in val_idx:
                return [val_idx[target-nums[i]], i]
            val_idx[nums[i]] = i
