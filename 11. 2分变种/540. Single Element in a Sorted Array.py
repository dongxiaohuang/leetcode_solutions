class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

# method 2
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums)-1
        while start +1 < end:
            mid = start + (end-start)//2
            if mid % 2 == 0: # mid is even
                if nums[mid] == nums[mid+1]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid] == nums[mid-1]:
                    start = mid
                else:
                    end = mid
        # print(nums[start],  nums[end])
        if start % 2 == 0:
            if nums[start] != nums[start+1]:
                return nums[start]
            else:
                return nums[end]
        else:
            if nums[start] != nums[start-1]:
                return nums[start]
            else:
                return nums[end]