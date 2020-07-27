class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start = 0
        end = len(nums)-1

        # 21
        while start < end-1:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid
        if nums[start] > nums[end]:
            return start
        else:
            return end
