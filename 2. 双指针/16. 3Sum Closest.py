class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = target - sum(nums[:3])
        for i in range(len(nums)):
            aim = target-nums[i]
            start = i+1
            end = len(nums)-1
            while start < end:
                diff = aim - nums[start] - nums[end]
                if diff == 0:
                    return target
                closest = diff if abs(diff) < abs(closest) else closest
                if diff < 0:
                    end -= 1
                else:
                    start += 1
        return target - closest
