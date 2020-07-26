class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if idx < len(nums):
                nums[idx] = - abs(nums[idx])

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
