class Solution:
    def trap(self, height: List[int]) -> int:
        leftmost = 0
        rightmost = 0
        right = len(height)-1
        left = 0
        res = 0
        while left < right:
            leftmost = max(leftmost, height[left])
            rightmost = max(rightmost, height[right])
            if leftmost < rightmost:
                res += leftmost - height[left]
                left += 1
            else:
                res += rightmost - height[right]
                right -= 1
        return res