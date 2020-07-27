class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return [-1, -1]
        start, end = 0, len(nums)-1
        begin, stop = -1, -1
        while start + 1 < end:
            mdl = start + (end-start)//2
            if nums[mdl] < target:
                start = mdl
            else:
                end = mdl
        if nums[end] == target:
            begin = end
        if nums[start] == target:
            begin = start
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mdl = start + (end-start)//2
            if nums[mdl] <= target:
                start = mdl
            else:
                end = mdl
        if nums[start] == target:
            stop = start
        if nums[end] == target:
            stop = end
        return [begin, stop]
