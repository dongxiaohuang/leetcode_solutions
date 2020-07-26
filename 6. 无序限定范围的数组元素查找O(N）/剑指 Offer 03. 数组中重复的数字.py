class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self,nums, duplication):
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                duplication[0] = idx
                return True
            else:
                nums[idx] = - abs(nums[idx])
        # print(duplication)
        return False