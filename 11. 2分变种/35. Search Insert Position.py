class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        start = 0
        end = len(nums)-1
        while start+1 < end:
            mdl = start + (end - start)//2
            if nums[mdl] < target:
                start = mdl
            else:
                end = mdl

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        if target < nums[start]:
            return start
        if target < nums[end]:
            return end
        return end+1
