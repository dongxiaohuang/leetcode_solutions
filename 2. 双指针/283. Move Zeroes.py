class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        start = 0
        cur = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[cur], nums[start] = nums[start], nums[cur]
                start += 1
