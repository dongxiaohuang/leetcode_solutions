class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_idx = 0
        two_idx = len(nums)-1
        idx= 0
        while idx <= two_idx:
            if nums[idx] == 0:
                nums[zero_idx], nums[idx] = nums[idx], nums[zero_idx] 
                zero_idx += 1
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            elif nums[idx] == 2:
                nums[two_idx], nums[idx] = nums[idx], nums[two_idx]
                two_idx -= 1