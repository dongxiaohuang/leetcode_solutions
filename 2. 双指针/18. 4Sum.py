class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4 > target:
                break
            for j in range(i+1, len(nums)-2):
                s = j+1
                e = len(nums)-1
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i]+nums[j]*3 > target:
                    break
                while s < e:
                    current_sum = nums[i] + nums[j] + nums[s] + nums[e]
                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[s], nums[e]])
                        while s < e and nums[s+1] == nums[s]:
                            s += 1
                        while s < e and nums[e-1] == nums[e]:
                            e -= 1
                        s += 1
                        e -= 1
                    elif current_sum < target:
                        s += 1
                    else:
                        e -= 1
        return res
